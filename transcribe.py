import whisper
import os
import sys

model = whisper.load_model("medium", device="cuda")

files = [
    {
        "audio": "/home/gabriel/Escritorio/Fundamentos de Ciencias/Clase 1/Clase 1 - Fundamentos de Ciencias.m4a",
        "output": "/home/gabriel/Escritorio/Fundamentos de Ciencias/Clase 1/Clase 1 - Fundamentos de Ciencias.md",
        "clase": "1",
    },
    {
        "audio": "/home/gabriel/Escritorio/Fundamentos de Ciencias/Clase 2/Clase 2 - Fundamentos de Ciencias.m4a",
        "output": "/home/gabriel/Escritorio/Fundamentos de Ciencias/Clase 2/Clase 2 - Fundamentos de Ciencias.md",
        "clase": "2",
    },
]

for f in files:
    print(f"\n{'='*60}")
    print(f"Transcribiendo: {os.path.basename(f['audio'])}")
    print(f"{'='*60}")
    sys.stdout.flush()

    result = model.transcribe(
        f["audio"],
        language="es",
        verbose=True,
    )

    audio_basename = os.path.basename(f["audio"])
    header = (
        f"# Transcripción — Clase {f['clase']} — Fundamentos de Ciencias\n\n"
        f"**Idioma:** español  \n"
        f"**Fuente:** `{audio_basename}`\n\n"
        f"---\n\n"
    )

    segments = result["segments"]
    paragraphs = []
    current_paragraph = []

    for seg in segments:
        text = seg["text"].strip()
        if not text:
            continue
        current_paragraph.append(text)
        if text.endswith((".", "?", "!", "…")) and len(" ".join(current_paragraph)) > 200:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []

    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    body = "\n\n".join(paragraphs)

    with open(f["output"], "w", encoding="utf-8") as out:
        out.write(header + body + "\n")

    print(f"\nGuardado: {f['output']}")
    sys.stdout.flush()

print("\n¡Transcripción completada para ambos archivos!")
