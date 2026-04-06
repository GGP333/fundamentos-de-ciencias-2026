# Apuntes de Estudio — Clase 2: Bases de Biología Molecular

**Curso:** Fundamentos de Ciencias para Ingeniería en Salud — 2026
**Fuentes integradas:**
- 📄 PDF: *Clase 1_Bases de Biol Mol_Fundamentos Cs Ing Salud 2026* (80 diapositivas)
- 🎤 Transcripción de audio: *Clase 2 - Fundamentos de Ciencias*

---

## 1. Objetivos de estudio

1. Explicar el **dogma central de la biología molecular** (flujo de información ADN → ARN → proteína) y sus excepciones/ampliaciones, incluyendo al ARN como molécula funcional en igualdad de condiciones con la proteína.
2. Comparar la organización celular y genética de **bacterias, arqueas y eucariotas** (compartimentalización, intrones, histonas, operones).
3. Describir el **código genético**: degenerado, 64 codones, codones de inicio/término, mutaciones conservadas vs. missense, marco de lectura.
4. Comprender la **síntesis de proteínas** (traducción): estructura del ribosoma, sitios A/P/E, iniciación, elongación, terminación, polisomas; el concepto de **doble código** (codón-anticodón + aminoacil-tRNA sintetasa).
5. Explicar la regulación de la expresión génica a tres niveles: **transcripcional** (factores de transcripción, promotores, enhancers), **epigenético** (metilación del ADN, modificaciones de histonas, heterocromatina/eucromatina) y **post-traduccional**.
6. Describir el sistema **CRISPR-Cas9** como sistema inmune de procariotas y como herramienta de edición génica.
7. Distinguir los mecanismos de **miRNA y siRNA** (interferencia de ARN), y la diferencia entre **knockdown** y **knockout**.

> 🎤 Clase — El profesor señaló que el enfoque principal de esta sesión es "cómo se regula la expresión de los genes", porque eso es lo que más harán como investigadores. Indicó que subirá artículos de revisión (especialmente de epigenética y CRISPR) y papers experimentales para el seminario.

---

## 2. Mapa conceptual

```
BASES DE BIOLOGÍA MOLECULAR
│
├─ Dogma central (no tan dogma)
│   ├─ ADN → ARN → Proteína (flujo clásico)
│   ├─ ADN → ADN (replicación)
│   ├─ ARN → ARN (replicación viral)
│   ├─ ARN → ADN (transcripción reversa)
│   ├─ 🎤 "El verdadero dogma: de proteína NO se vuelve a ácido nucleico"
│   └─ ARN como destino funcional (no solo intermedio)
│       └─ Ribozimas, rRNA, tRNA, miRNA, siRNA...
│
├─ Compartimentalización
│   ├─ Procariotas (bacterias, arqueas): un compartimento
│   │   └─ Transcripción y traducción simultáneas
│   └─ Eucariotas: transcripción en núcleo, traducción en citoplasma
│       └─ ARNm debe salir por poros nucleares
│
├─ Tabla comparativa: Bacteria / Archaea / Eucarya
│   ├─ Cromosoma: 1 circular / 1 circular / múltiples lineales
│   ├─ Intrones: No / Solo en tRNA / Sí (mayoría de genes)
│   ├─ Histonas/nucleosomas: No / Sí / Sí
│   ├─ Iniciador: fMet / Met / Met
│   └─ 🎤 "Arqueas comparten rasgos con eucariotas → ancestro común"
│
├─ Código genético
│   ├─ Degenerado: varios codones → 1 aminoácido
│   ├─ 64 codones: 61 para aa + 3 de término (UAA, UGA, UAG)
│   ├─ Codón de inicio: AUG (Met); también GUG en mamíferos
│   └─ Doble código: codón-anticodón + aminoacil-tRNA sintetasa
│
├─ Ribosoma y síntesis de proteínas
│   ├─ Subunidad mayor + menor → sitios A, P, E
│   ├─ Velocidad: 3-5 aa/seg; titina (30.000 aa): 2-3 h
│   ├─ Enlace peptídico catalizado por rRNA (ribozima)
│   └─ Polisomas: múltiples ribosomas en un ARNm → eficiencia
│
├─ Regulación de la expresión génica
│   ├─ Transcripcional: factores de transcripción + promotor + enhancer
│   │   └─ Footprinting para identificar sitios de unión
│   ├─ Epigenética
│   │   ├─ Metilación del ADN (islas CpG)
│   │   ├─ Modificaciones de histonas (fosforilación, acetilación, metilación)
│   │   ├─ Heterocromatina (cerrada) vs. eucromatina (abierta)
│   │   └─ 🎤 "Enzimas que borran y enzimas que pintan la epigenética"
│   ├─ Post-traduccional: degradación, fosforilación, corte proteolítico
│   └─ ARN regulatorios
│       ├─ miRNA (codificado en genoma) / siRNA (exógeno o experimental)
│       ├─ DICER + ARGONAUTA → degradan ARNm blanco
│       └─ Knockdown (reducción) vs. Knockout (eliminación del gen)
│
├─ CRISPR-Cas9
│   ├─ Sistema inmune adaptativo de procariotas
│   ├─ Secuencias palindrómicas + espaciadores (de fagos)
│   ├─ crRNA guía + Cas9 → corta ADN del virus invasor
│   ├─ Herramienta de edición génica en eucariotas
│   │   └─ Requiere: ARN guía + expresión de Cas9 + secuencias PAM
│   └─ 🎤 "Premio Nobel 2020: Doudna y Charpentier + Mojica (español)"
│
└─ Antibióticos que atacan al ribosoma (📄 PDF, poco en audio)
    ├─ Estreptomicina: inhibe iniciación (procariotas)
    ├─ Cloranfenicol: inhibe peptidil transferasa 50S
    ├─ Cicloheximida: inhibe peptidil transferasa 60S (eucariotas)
    ├─ Eritromicina: inhibe translocación
    └─ Puromicina: análogo de aminoacil-tRNA, termina cadena prematuramente
```

---

## 3. Desarrollo por bloques temáticos

### 3.1 Dogma central de la biología molecular

📄 PDF — Diapositivas 1–2: "Dogma Central (no tan dogma)"; cita de Crick: "Once information has got into a protein it can't get out again."

El llamado "dogma central" describe el **flujo de información genética**:

- **ADN → ARN** (transcripción)
- **ARN → Proteína** (traducción)
- **ADN → ADN** (replicación)
- **ARN → ARN** (replicación de virus de ARN)
- **ARN → ADN** (transcripción reversa)

El **verdadero dogma** (lo que no ocurre) es: **proteína → ácido nucleico**. La información no fluye de vuelta desde la proteína hacia ARN o ADN.

🎤 Clase — El profesor mostró el esquema original de Crick (fines de los años 50) donde ya se predecían estos flujos. Enfatizó que el ARN **no es solo un intermediario** para hacer proteínas: "Yo lo pongo en igualdad de condiciones funcionales con la proteína." Existe una gran cantidad de genes que codifican ARN funcionales (no proteínas): rRNA, tRNA, miRNA, siRNA, ribozimas, etc. La hipótesis del "mundo de ARN" propone que las primeras moléculas complejas en la evolución fueron ARN, y las primeras enzimas probablemente fueron ribozimas.

También mencionó que un flujo directo ADN → Proteína no está totalmente descartado teóricamente, pero no se han encontrado evidencias naturales de esto.

---

### 3.2 Compartimentalización: procariotas vs. eucariotas

📄 PDF — Diapositivas 3–4: tabla comparativa bacteria/arquea/eucariota; organización de transcripción y traducción.

| Característica | Bacteria | Arquea | Eucariota |
|---|---|---|---|
| Estructura celular | Procariota | Procariota | Eucariota |
| Cromosoma | 1, circular | 1, circular | Múltiples, lineales |
| Ácidos grasos de membrana | Lineales | Ramificados | Lineales |
| Intrones | No | Solo en genes de ARNt | Sí, en mayoría de genes |
| Histonas/nucleosomas | No | Sí | Sí |
| Primer aminoácido | Formil-metionina (fMet) | Metionina | Metionina |
| ARN polimerasas | 1 (4–5 subunidades) | 1 (8–14 subunidades) | Varias (12–14 subunidades) |
| Sensible a estreptomicina/cloranfenicol | Sí | No (resistente) | No (resistente) |
| Sensible a toxina diftérica | No (resistente) | Sí | Sí |

**Diferencia fundamental en la expresión génica:**
- **Procariotas**: transcripción y traducción ocurren en el **mismo compartimento**, frecuentemente de manera **simultánea**.
- **Eucariotas**: la transcripción ocurre en el **núcleo**; el ARNm debe procesarse (eliminar intrones → splicing) y salir por los **poros nucleares** para traducirse en el **citoplasma** en los ribosomas.

🎤 Clase — Se enfatizó que las arqueas comparten rasgos con los eucariotas (histonas, intrones en tRNA, factores de elongación similares, sensibilidad a toxina diftérica), reflejando que en el árbol evolutivo **arqueas y eucariotas comparten un ancestro común** más reciente que con las bacterias. Los tres dominios de la vida son: Bacteria, Archaea y Eucarya.

Sobre las arqueas: sus ácidos grasos de membrana son **ramificados**, lo que les confiere estabilidad a altas temperaturas (organismos extremófilos), aunque existen bacterias termófilas que no tienen esta característica.

---

### 3.3 Organización génica: operones vs. genes distribuidos

📄 PDF — Diapositivas 4–5: comparación de la organización, transcripción y traducción en procariotas y eucariotas.

**En bacterias — Operón (ej. operón del triptófano):**
- Los genes que codifican enzimas de una misma vía metabólica están **contiguos** en el cromosoma, en el mismo locus.
- Se transcriben en un **solo ARNm policistrónico** (un ARN que codifica múltiples proteínas).
- Al traducirse, se producen varias proteínas diferentes a partir de ese único ARNm.

**En eucariotas:**
- Los genes equivalentes están **distribuidos en distintos cromosomas**.
- Cada gen produce su propio ARNm (**monocistrónico**: un ARN → una proteína, en general).
- Aunque existen excepciones: algunos ARNm eucariotas producen más de una proteína (splicing alternativo, IRES), un tema "super relevante en biología actual".

🎤 Clase — Se usó como ejemplo el operón del triptófano: en *E. coli* los genes trpA-trpE están juntos y se transcriben como una unidad. En levaduras, esos mismos genes están repartidos en distintos cromosomas.

---

### 3.4 Watson y Crick — historia y contexto

📄 PDF — Diapositivas 6–7: el modelo de Watson y Crick, doble hélice.

🎤 Clase — El profesor hizo una mención extensa al paper original de Watson y Crick (1953, *Nature*). Destacó:
- No solo describieron la doble hélice, sino que sugirieron cómo se podía copiar y leer → origen del concepto de flujo de información.
- El paper de **Rosalind Franklin** estaba en el mismo número (*issue*) de *Nature*. Ella obtuvo la imagen de difracción de rayos X (foto 51) que fue clave.
- Franklin interpretaba la estructura como una hélice simple; Watson y Crick vieron que era **doble hélice**.
- El profesor recomendó leer el paper original: "Uno se da cuenta del pensamiento de esta gente."
- Reconoció la controversia ética ("fueron unos pillos") pero defendió la genialidad del razonamiento.

---

### 3.5 Código genético

📄 PDF — Diapositivas 8–9, 27–31: el código genético degenerado, desciframiento histórico.

**Propiedades del código genético:**
- Cada codón consta de **3 bases nitrogenadas** (triplete).
- De los **64 codones** posibles: **61 codifican aminoácidos** y **3 son codones de término** (stop): UAA, UGA, UAG.
- Es **degenerado**: la mayoría de los aminoácidos están codificados por más de un codón.
  - Ej.: serina puede usar 4 codones (UCU, UCC, UCA, UCG).
  - La degeneración ocurre predominantemente en la **tercera posición** del codón.
- **Codón de inicio**: AUG (metionina) es el más común en todos los organismos. También GUG y CUG en algunos mRNAs de bacterias y eucariotas.

**Consecuencias de la degeneración:**
- **Mutaciones sinónimas** (conservadas/silenciosas): cambio en la base del codón que **no cambia** el aminoácido (ej. UCU → UCA, ambos = Ser). Mayor "seguridad" frente a errores.
- **Mutaciones missense** (no sinónimas): cambio que **sí altera** el aminoácido incorporado a la proteína.

**Marco de lectura:**
- Definido por el codón de inicio hasta el codón de término.
- Teóricamente un ARNm puede tener hasta 3 marcos de lectura posibles.
- Un corrimiento del marco de lectura (inserción o deleción de 1–2 bases) altera toda la proteína downstream.

📄 PDF — Diapositivas 30–31: Nirenberg y Khorana descifraron el código genético con ARNm sintéticos y trinucleótidos + todos los componentes para síntesis proteica in vitro. Nirenberg demostró que poli-U codifica para fenilalanina; Khorana con ARNm de 2 bases alternadas demostró que el codón es un triplete.

🎤 Clase — "Imaginen en los años 60–70, la gente tenía que usar esta tabla pegada en la pared para identificar aminoácidos. Ahora todo es bioinformática y con inteligencia artificial ya ni necesitas ser bioinformático para analizar secuencias."

---

### 3.6 Ribosoma y síntesis de proteínas (traducción)

📄 PDF — Diapositivas 9–10, 42–65: estructura del ribosoma, iniciación, elongación, terminación, polisomas.

**El ribosoma:**
- Complejo de **ARN ribosomal (rRNA) + proteínas** → ribonucleoproteína.
- Dos subunidades: **mayor y menor**, que se ensamblan al iniciar la traducción.
- Tres sitios funcionales: **A** (aminoacil, entrada), **P** (peptidil, enlace peptídico), **E** (exit, salida).

**Velocidad de traducción:**
- 3–5 aminoácidos por segundo.
- Proteínas de 100–200 aa: menos de 1 minuto.
- **Titina** (la proteína más grande, ~30.000 aa, del músculo/sarcómero): 2–3 horas.

🎤 Clase — Se preguntó en clase qué es la titina. El profesor explicó que es una proteína gigante del sarcómero muscular que conecta los componentes (miosina, actina) y resiste el estiramiento.

**Iniciación en bacterias:**
- Factores de iniciación IF1, IF2, IF3 se unen a la subunidad 30S.
- fMet-tRNAi^Met se posiciona guiado por la **secuencia de Shine-Dalgarno** (complementaria al rRNA 16S).
- Se ubica el codón AUG de inicio; se agrega la subunidad 50S → complejo de iniciación 70S.
- El tRNA iniciador queda en el sitio P, listo para recibir el siguiente aminoacil-tRNA en el sitio A.

**Iniciación en eucariotas:**
- Más compleja; involucra la **cápsula 5′ metilada** (7-metilguanilato) del ARNm.
- Formación del **complejo ternario** (eIF2-GTP-Met-tRNAi).
- Múltiples factores de iniciación eucariotas (eIFs).

📄 PDF — Diapositivas 48–55: pasos detallados de iniciación y elongación.

**Elongación** (altamente conservada en los tres dominios):
1. El aminoacil-tRNA correcto entra al sitio A como complejo ternario con EF-Tu-GTP.
2. Hidrólisis de GTP → el aminoacil-tRNA se acomoda en el sitio A.
3. Se forma el **enlace peptídico** (catalizado por el rRNA → actividad de ribozima).
4. **Translocación**: EF-G-GTP desplaza los tRNAs (P→E, A→P); el tRNA vacío sale por E.
5. Ciclo se repite.

**Terminación:**
- Un codón de término (UAA, UGA, UAG) llega al sitio A.
- **Factores de liberación** (RF1/RF2 en bacterias) reconocen el codón stop.
- RF3-GTP cataliza la liberación de la cadena polipeptídica y la disociación del ribosoma.

**Polisomas:**
- Múltiples ribosomas traduciendo simultáneamente el mismo ARNm.
- En eucariotas, los polisomas suelen ser **circulares** (interacción de la cola poli-A con la cápsula 5′).
- Representan la fracción de ribosomas con **alta tasa de síntesis** (más activos).

🎤 Clase — Se explicó cómo separar polisomas mediante gradientes de densidad (sacarosa) y ultracentrifugación: las fracciones más pesadas contienen los polisomas activos.

---

### 3.7 El doble código: aminoacil-tRNA sintetasas

📄 PDF — Diapositivas 33–36: estructura del tRNA, aminoacil-tRNA sintetasa, proceso de dos pasos.

La traducción requiere **dos códigos**, no uno:

1. **Código codón-anticodón**: el anticodón del tRNA reconoce el codón del ARNm por complementariedad de bases en el ribosoma.
2. **Código de carga del tRNA**: la enzima **aminoacil-tRNA sintetasa** reconoce específicamente un tRNA y le une el aminoácido correcto.

Hay una aminoacil-tRNA sintetasa específica para **cada aminoácido**, y cada una reconoce todos los tRNAs afines (isoaceptores) para ese aminoácido.

**Estructura del tRNA:**
- Forma de "hoja de trébol" con un anticodón en un extremo y la secuencia **CCA** en el extremo 3′ donde se une el aminoácido.
- Contiene nucleótidos modificados: dihidrouridina (D), inosina (I), pseudouridina (ψ), etc.
- Se han identificado 30–40 tRNA en bacterias y 50–100 en células animales y vegetales.
- Algunos tRNA reconocen más de un codón (gracias a la **inosina** en la posición de wobble del anticodón, que puede aparearse con A, C o U).

📄 PDF — Diapositivas 28–29: dos tipos de Met-tRNA (iniciador tRNAi^Met y elongador tRNA^Met); fMet solo en bacterias.

🎤 Clase — El profesor enfatizó que este segundo código es ignorado frecuentemente: "Todo el mundo habla de codones y anticodones, pero cómo le pegas el aminoácido correcto al tRNA correcto también es un código, y es igual de fundamental." Las aminoacil-tRNA sintetasas deben reconocer tanto el aminoácido como el tRNA específico.

---

### 3.8 ARN como ribozima — hipótesis del mundo de ARN

📄 PDF — Diapositivas 11–14: hipótesis ribozima, propiedades catalíticas del ARN, enlace peptídico en el ribosoma.

- **1989**: Altman y Cech reciben el Premio Nobel de Química por descubrir las propiedades catalíticas del ARN.
- El ARN puede:
  - Autoduplicarse o duplicar otras moléculas de ARN.
  - Catalizar reacciones químicas sencillas.
  - Realizar enlaces peptídicos.

**Demostración clave en el ribosoma:**
- Por cristalografía se demostró que el **sitio activo** donde se forma el enlace peptídico en el ribosoma **no contiene proteínas** (la única proteína presente es la cadena naciente que se está formando).
- El enlace peptídico es catalizado por el **rRNA** → el ribosoma es una **ribozima**.
- El 2′-OH de la A76 del aminoacil-tRNA en el sitio P forma puentes de hidrógeno con el grupo α-amino del aminoacil-tRNA en el sitio A, orientando correctamente los aminoácidos.

🎤 Clase — "La gente pensaba que eran proteínas del ribosoma las que catalizaban el enlace peptídico, pero se demostró que es el propio ARN ribosomal. Esto es una demostración más de que el ARN tiene capacidad enzimática."

---

### 3.9 Regulación de la expresión génica — factores de transcripción

📄 PDF — Diapositivas 15–16: factores de transcripción, diversidad, DNAase footprinting.

**Concepto central:** todas las células de un organismo tienen el **mismo material genético**, pero las diferencias funcionales (neurona vs. hepatocito vs. linfocito) se deben a **cómo se regula la expresión de cada gen**.

**Tres niveles de regulación:**
1. **Transcripcional** (el más estudiado): controla si un gen se transcribe o no.
2. **Traduccional**: el ARNm existe pero no se traduce (o se traduce a distinta tasa).
3. **Post-traduccional**: la proteína se degrada, modifica, corta, etc.

Los **factores de transcripción** son proteínas que se unen a regiones específicas del ADN para activar o reprimir la transcripción de un gen.

**Componentes de la regulación transcripcional:**
- **Promotor**: secuencia del ADN cercana al gen donde se ensambla la maquinaria de transcripción (ARN polimerasa + factores basales).
- **Enhancers** (potenciadores): secuencias que pueden estar **muy alejadas** del gen (aguas arriba o abajo, miles de nucleótidos); mejoran la transcripción. No son obligatorios, pero su presencia aumenta significativamente la tasa de transcripción.
- Los factores de transcripción tienen un **dominio de unión al ADN** con afinidad por secuencias específicas.
- Se ensamblan complejos multiproteicos sobre el promotor, y el plegamiento de la cromatina puede acercar enhancers lejanos.

**DNAase footprinting** (técnica experimental):
- Se trata un fragmento de ADN con DNasa (enzima que degrada ADN).
- Las zonas donde hay proteínas unidas quedan **protegidas** de la degradación.
- Al separar los fragmentos en un gel de electroforesis, las zonas protegidas aparecen como "huellas" (footprints).
- Permite identificar qué regiones del ADN tienen proteínas reguladoras unidas.

🎤 Clase — El profesor mostró la diversidad de factores de transcripción humanos (referencia: Lambert et al., *Cell* 2018). Enfatizó que estos factores son una familia enorme de proteínas, y que cuando él estudió "nadie hablaba de epigenética, pero todo el mundo hablaba de factores de transcripción". También aclaró que la DNasa no degrada proteínas, solo ADN (ante una pregunta de la clase).

---

### 3.10 Epigenética

📄 PDF — Diapositivas 17–19: regulación epigenética, cromatina, CRISPR.

La epigenética es una **capa de regulación superior** a los factores de transcripción. Es como poner parte del genoma "en una caja fuerte": esos genes no están disponibles para ser regulados por los factores de transcripción, sin importar cuáles factores estén presentes.

**Heterocromatina y eucromatina:**
- **Heterocromatina** (condensada, generalmente en la periferia del núcleo): genes "dormidos", no disponibles para transcripción.
- **Eucromatina** (descondensada, más al centro del núcleo): genes accesibles para transcripción.
- La proporción de hetero/eucromatina **cambia** según el tipo celular, el momento del ciclo celular, el estrés y otros factores.

**Niveles de condensación del ADN:**
Doble hélice → enrollamiento en nucleosomas (histonas) → fibra de 30 nm → bucles → cromosoma condensado (solo durante mitosis; normalmente no están así).

**Mecanismos epigenéticos principales:**

| Mecanismo | Dónde actúa | Efecto |
|---|---|---|
| **Metilación del ADN** | Bases C y G (especialmente islas CpG) | Generalmente silencia la transcripción |
| **Fosforilación de histonas** | Proteínas histonas | Puede aumentar o disminuir el remodelamiento de cromatina |
| **Acetilación de histonas** | Proteínas histonas | Generalmente abre la cromatina (activa transcripción) |
| **Metilación de histonas** | Proteínas histonas | Puede activar o reprimir según el residuo |

🎤 Clase — El profesor explicó extensamente:
- Las modificaciones de histonas son **post-traduccionales** (fosforilación, acetilación, metilación de proteínas). La metilación del ADN es diferente: actúa directamente sobre las bases del ADN.
- Existen enzimas que **"pintan"** (agregan marcas epigenéticas) y enzimas que **"borran"** (las eliminan). Regulando estas enzimas se controla la expresión.
- **Islas CpG**: zonas del ADN ricas en C y G → mayor probabilidad de metilación → regulación.
- La metilación del ADN es el mecanismo epigenético más estudiado y típico.

**Epigenética y ambiente:**
- Factores ambientales (alimentación, estrés, exposición a tóxicos) pueden modificar las marcas epigenéticas.
- Ejemplo clásico en ratones: madres obesas alimentadas con dieta grasa durante la gestación producen crías con problemas cognitivos y metabólicos.
- Ejemplo histórico en humanos: mujeres que sufrieron hambruna durante la guerra (posiblemente la Hambruna Holandesa de 1944–45) tuvieron hijas con caderas más estrechas → limitación reproductiva transgeneracional.

**Transmisión epigenética transgeneracional:**
- Demostrada en organismos pequeños (gusanos, moscas).
- En humanos: hay indicios pero **no está demostrado definitivamente**. En mamíferos, lo que sí está claro es que el ambiente durante la gestación puede modificar la epigenética del embrión.

**Epigenética y cáncer:**
- Existen genes marcadores de mayor probabilidad de desarrollar cáncer.
- Gemelos idénticos (mismo genoma) pueden diferir: uno desarrolla cáncer y otro no → la epigenética (influenciada por ambiente, alimentación) determina si esos genes se expresan o no.
- La radiación produce mutaciones directas en el ADN (no es epigenética stricto sensu, sino alteración genómica).

🎤 Clase — El profesor recomendó una edición especial de *Investigación y Ciencia* (versión en español de *Scientific American*) dedicada a epigenética. "En español, fácil de leer, super bien hecho." Lo subirá al aula virtual. Indicó que en Chile hay poca investigación de epigenética a nivel molecular (la mayoría trabaja a nivel macro/epidemiológico) y sugirió que es un buen campo de investigación.

---

### 3.11 CRISPR-Cas9

📄 PDF — Diapositiva 19–20: repeticiones palindrómicas cortas agrupadas y regularmente interespaciadas.

**CRISPR** = *Clustered Regularly Interspaced Short Palindromic Repeats* (repeticiones palindrómicas cortas agrupadas y regularmente interespaciadas).

**Como sistema inmune de procariotas:**

1. Un **bacteriófago** (virus) infecta una bacteria.
2. La mayoría de las bacterias mueren, pero algunas sobreviven e **insertan un fragmento del ADN viral** en su genoma, entre las repeticiones palindrómicas (estos fragmentos se llaman **espaciadores**).
3. Esa información se hereda a las siguientes generaciones.
4. Cuando el **mismo tipo de virus** vuelve a infectar, la bacteria ya tiene la secuencia viral en su genoma.
5. Se transcribe un **crRNA** (CRISPR RNA, o ARN guía) complementario al genoma del virus.
6. El crRNA se une al ADN viral invasor por complementariedad, y la proteína **Cas9** (una endonucleasa) **corta** el ADN viral → el virus no puede reproducirse.

Es un **sistema inmune adaptativo con memoria** — análogo conceptual al sistema inmune adaptativo de los animales.

**Distribución:** ~100% de las arqueas y ~60% de las bacterias tienen CRISPR. Ningún eucariota tiene el sistema de forma natural (aunque se encontró en el genoma mitocondrial, que tiene origen bacteriano).

**Descubrimiento histórico:**
- Años 80: japoneses descubren secuencias palindrómicas repetidas en genomas bacterianos; las usan para clasificar bacterias.
- **Francisco Mojica** (español): identificó los espaciadores como secuencias de bacteriófagos e infirió la función inmune.
- **Premio Nobel 2020**: Jennifer Doudna y Emmanuelle Charpentier (el profesor no recordó si Mojica fue incluido; en efecto, no lo fue en el Nobel, aunque su contribución es reconocida).

**CRISPR como herramienta de edición génica en eucariotas:**
- Los eucariotas **no expresan Cas9** → hay que introducirla exógenamente.
- Se necesita: (1) un **ARN guía** diseñado para la secuencia blanco, (2) expresión de **Cas9**, (3) presencia de secuencias **PAM** (*Protospacer Adjacent Motif*) cercanas al sitio de corte (estas sí existen en eucariotas por probabilidad estadística — son secuencias cortas).
- Herramientas bioinformáticas permiten diseñar ARN guías minimizando el riesgo de **off-target** (cortes en lugares no deseados del genoma) — principal preocupación de seguridad.
- Ya se usa en **terapia génica** para anemia falciforme y otras enfermedades; está aprobado por algunas agencias regulatorias.

🎤 Clase — El profesor mencionó un paper donde usaron CRISPR en ratones sordos para restaurar la audición modificando un gen. Recomendó revisar la **Nobel Foundation** (nobelprize.org): "Ahí aparece el discurso, el video de aceptación y un resumen escrito de manera fácil para entenderlo. Está super bueno."

---

### 3.12 miRNA y siRNA — interferencia de ARN

📄 PDF — Diapositivas 20–26: inhibición de la síntesis de proteínas por miRNA y siRNA.

#### Historia del descubrimiento
- En los años 80–90, para silenciar un gen se usaba **antisentido** (una hebra de ARN complementaria al ARNm blanco que bloqueaba su traducción).
- Por error, alguien mezcló el antisentido con el sentido → se formó **ARN de doble hebra** (dsRNA).
- El resultado fue **mejor** que el antisentido solo → se descubrió que la célula tiene maquinaria para procesar dsRNA.

#### Mecanismo de interferencia de ARN:

1. La enzima **DICER** reconoce ARN de doble hebra y lo corta en fragmentos de ~21 nucleótidos.
2. Los fragmentos se separan en hebras simples.
3. Una hebra se incorpora al complejo **RISC** (que incluye la proteína **ARGONAUTA**).
4. Si la hebra es complementaria a un ARNm blanco → el ARNm es **degradado** o su traducción es **bloqueada**.

#### siRNA vs. miRNA

| Característica | siRNA | miRNA |
|---|---|---|
| Origen | Exógeno (experimental, viral) o introducido artificialmente | Codificado en el genoma del organismo |
| Estructura inicial | dsRNA largo | Pre-miRNA (hairpin/horquilla con imperfecciones) |
| Procesamiento | DICER corta dsRNA largo | DICER procesa pre-miRNA en miRNA maduro |
| Función | Silenciamiento experimental o defensa antiviral | Regulación endógena de la expresión génica |
| Complementariedad | Generalmente perfecta | Frecuentemente imperfecta → regulación más que degradación |

**miRNA codificados en el genoma:**
- Existen genes que codifican para estos ARN regulatorios, no para proteínas.
- Un mismo miRNA puede expresarse en ciertos tejidos y no en otros (expresión tejido-específica).
- Algunos miRNA son ubicuos; otros son altamente específicos de un tipo celular.
- Se identifica cuáles ARN están asociados a polisomas (fracción activa de traducción) para detectar miRNAs que están regulando la traducción.

🎤 Clase — Se mencionaron los nombres mi-R-1, mi-R-124, mi-R-128, etc. El profesor explicó que ya existen kits comerciales para purificar miRNAs (Thermo, Qiagen) y técnicas de secuenciación del **mirtoma** completo (todo el conjunto de miRNAs de una célula).

#### Knockdown vs. Knockout

| Término | Definición |
|---|---|
| **Knockdown** | **Reducción** de la expresión de un gen (el gen sigue presente; se reduce su producto). Se logra con siRNA/miRNA. Imperfecto: no elimina al 100%. |
| **Knockout** | **Eliminación** del gen o de su función (deleción genómica). Se puede lograr con CRISPR-Cas9. La proteína desaparece por completo. |

🎤 Clase — El profesor insistió en esta diferencia: "El siRNA produce un knockdown porque es imperfecto — reduce pero no elimina. El knockout es cuando el gen desaparece o se lesiona." Si uno inserta un gen de miRNA en el genoma (que produzca interferencia constitutiva), es "como un knockdown permanente, pero sigue sin ser un knockout porque el gen blanco está intacto".

---

### 3.13 Antibióticos que atacan al ribosoma

📄 PDF — Diapositivas 75–79. *Del material oficial (poco desarrollado en la grabación).*

Más de la mitad de los antibióticos actuales atacan el ribosoma, principalmente la subunidad grande.

| Antibiótico | Mecanismo |
|---|---|
| **Estreptomicina** (y aminoglucósidos) | Inhibe iniciación y causa lectura errónea del ARNm (procariotas) |
| **Tetraciclina** | Se une a la subunidad 30S; inhibe unión de aminoacil-tRNAs (procariotas) |
| **Cloranfenicol** | Inhibe peptidil transferasa de la subunidad 50S (procariotas) |
| **Cicloheximida** | Inhibe peptidil transferasa de la subunidad 60S (eucariotas) |
| **Eritromicina** | Se une a la subunidad 50S; inhibe translocación (procariotas) |
| **Puromicina** | Análogo de aminoacil-tRNA; causa terminación prematura (procariotas Y eucariotas) |

**Toxina diftérica:** bloquea la síntesis proteica en eucariotas catalizando la transferencia de ADP-ribosa (desde NAD⁺) a diftamida, un residuo modificado del factor de elongación 2 (EF-2/translocasa).

---

## 4. Definiciones, convenciones y "memorizar sí o sí"

| Concepto | Definición / Dato clave |
|---|---|
| **Dogma central** | De proteína NO se puede generar ARN ni ADN. Todo lo demás puede ocurrir. |
| **Transcripción** | ADN → ARN (mediada por ARN polimerasa) |
| **Traducción** | ARN → Proteína (en el ribosoma) |
| **Replicación** | ADN → ADN |
| **Transcripción reversa** | ARN → ADN (retrovirus) |
| **Codón** | Triplete de bases del ARNm que especifica un aminoácido o señal de término |
| **Anticodón** | Triplete del tRNA complementario al codón |
| **Código degenerado** | Varios codones pueden codificar el mismo aminoácido |
| **Codón de inicio** | AUG (Met); también GUG (en bacterias y mamíferos) |
| **Codones de término** | UAA, UGA, UAG — no codifican aminoácidos |
| **64 codones** | 61 para aminoácidos + 3 de término |
| **fMet** | Formil-metionina; primer aminoácido en bacterias |
| **Operón** | Grupo de genes contiguos transcritos en un solo ARNm policistrónico (procariotas) |
| **Intrón** | Secuencia de ADN que se transcribe pero se elimina del ARNm maduro (splicing) |
| **Exón** | Secuencia que permanece en el ARNm maduro y codifica proteína o ARN funcional |
| **Histona** | Proteína alrededor de la cual se enrolla el ADN formando nucleosomas |
| **Nucleosoma** | Unidad de cromatina: 147 pb de ADN enrollados alrededor de un octámero de histonas |
| **Heterocromatina** | Cromatina condensada; genes silenciados |
| **Eucromatina** | Cromatina descondensada; genes accesibles |
| **Factor de transcripción** | Proteína que se une al ADN para activar o reprimir la transcripción |
| **Promotor** | Secuencia del ADN donde se ensambla la maquinaria de transcripción |
| **Enhancer** | Secuencia reguladora que potencia la transcripción, puede estar lejos del gen |
| **Metilación del ADN** | Adición de grupo metilo a bases C (especialmente en islas CpG); silencia genes |
| **Isla CpG** | Región del ADN con alta frecuencia de dinucleótidos CG; sitio preferente de metilación |
| **CRISPR** | Repeticiones palindrómicas cortas agrupadas y regularmente interespaciadas |
| **Cas9** | Endonucleasa guiada por ARN que corta ADN; proteína efectora del sistema CRISPR |
| **PAM** | *Protospacer Adjacent Motif*; secuencia corta necesaria cerca del sitio de corte de Cas9 |
| **Off-target** | Corte de Cas9 en una posición no deseada del genoma |
| **crRNA / ARN guía** | ARN complementario al ADN blanco que guía a Cas9 |
| **miRNA** | MicroARN endógeno (~21 nt) codificado en el genoma; regula expresión post-transcripcional |
| **siRNA** | Small Interfering RNA (~21 nt); generalmente exógeno o experimental |
| **DICER** | Enzima que corta dsRNA en fragmentos de ~21 nt |
| **ARGONAUTA** | Proteína del complejo RISC que media la degradación del ARNm blanco |
| **RISC** | Complejo proteico que ejecuta la interferencia de ARN |
| **Knockdown** | Reducción de la expresión de un gen (gen intacto, producto reducido) |
| **Knockout** | Eliminación del gen o su función (deleción genómica) |
| **Ribozima** | ARN con actividad catalítica (enzimática) |
| **Polisoma** | Múltiples ribosomas traduciendo un mismo ARNm simultáneamente |
| **Aminoacil-tRNA sintetasa** | Enzima que une el aminoácido correcto a su tRNA correspondiente |
| **Transcriptoma** | Conjunto de todos los ARNm expresados en una condición/tipo celular |
| **Proteoma** | Conjunto de todas las proteínas expresadas en una condición/tipo celular |

---

## 5. Preguntas tipo evaluación

### Preguntas cortas

**P1.** ¿Cuál es el verdadero "dogma" del dogma central? ¿Qué flujo de información NO ocurre?
> **R:** El verdadero dogma es que la información **no puede fluir desde la proteína hacia los ácidos nucleicos** (proteína → ARN o proteína → ADN no ocurre). Todos los demás flujos (ADN→ARN, ARN→Proteína, ADN→ADN, ARN→ARN, ARN→ADN) sí ocurren.

**P2.** ¿Por qué se dice que el código genético es "degenerado"? Dé un ejemplo.
> **R:** Porque la mayoría de los aminoácidos pueden ser codificados por más de un codón. Ejemplo: serina (Ser) es codificada por UCU, UCC, UCA, UCG (4 codones). Esto proporciona cierta robustez frente a mutaciones (mutaciones silenciosas en la tercera posición del codón).

**P3.** Explique por qué la traducción del ARNm requiere un "doble código".
> **R:** El primer código es la complementariedad **codón-anticodón** (ARNm-tRNA) en el ribosoma. El segundo código es el reconocimiento del tRNA por la **aminoacil-tRNA sintetasa**, que le une el aminoácido correcto. Sin este segundo código, no habría garantía de que el tRNA lleve el aminoácido que le corresponde.

**P4.** ¿Cuál es la diferencia fundamental entre la compartimentalización de la expresión génica en procariotas y eucariotas?
> **R:** En procariotas, transcripción y traducción ocurren en el mismo compartimento (citoplasma), frecuentemente de manera simultánea. En eucariotas, la transcripción ocurre en el núcleo y la traducción en el citoplasma; el ARNm debe procesarse (eliminar intrones) y exportarse por los poros nucleares.

**P5.** ¿Qué es la epigenética y por qué gemelos idénticos pueden ser fenotípicamente distintos?
> **R:** La epigenética es un nivel de regulación que determina qué genes están accesibles para ser transcritos (eucromatina) y cuáles están silenciados (heterocromatina), sin cambiar la secuencia del ADN. Gemelos idénticos tienen el mismo genoma, pero factores ambientales (dieta, estrés, exposiciones) modifican las marcas epigenéticas (metilación del ADN, modificaciones de histonas) de manera diferente, produciendo fenotipos distintos.

**P6.** Describa cómo funciona el sistema CRISPR como sistema inmune en bacterias.
> **R:** Cuando un fago infecta una bacteria, algunas bacterias sobrevivientes insertan un fragmento del ADN viral como espaciador entre las repeticiones palindrómicas de su genoma. En una infección posterior por el mismo fago, ese espaciador se transcribe como crRNA (ARN guía), que es complementario al genoma del virus. El crRNA guía a la proteína Cas9 (endonucleasa) hacia el ADN viral, que es cortado y destruido. Es un sistema inmune adaptativo con memoria.

**P7.** ¿Cuál es la diferencia entre knockdown y knockout?
> **R:** Knockout = eliminación completa del gen (ej. deleción con CRISPR); la proteína desaparece. Knockdown = reducción de la expresión del gen (ej. con siRNA o miRNA); el gen está intacto pero su producto se reduce. El knockdown es imperfecto (no llega al 100%).

**P8.** ¿Por qué el ribosoma se considera una ribozima?
> **R:** Porque por cristalografía se demostró que el sitio activo donde se forma el enlace peptídico está compuesto exclusivamente por ARN ribosomal (rRNA), sin proteínas del ribosoma involucradas en la catálisis. El ARN del ribosoma cataliza directamente la formación del enlace peptídico.

**P9.** Un ARNm tiene la secuencia 5′-AUGUCUUUAGCG...-3′. ¿Cuáles son los primeros aminoácidos?
> **R:** AUG = Met, UCU = Ser, UUA = Leu, GCG = Ala. La proteína comienza: Met-Ser-Leu-Ala...

---

## 6. Glosario

| Término | Definición breve |
|---|---|
| Aminoacil-tRNA sintetasa | Enzima que carga el aminoácido correcto en su tRNA correspondiente |
| Anticodón | Triplete del tRNA que se aparea con el codón del ARNm |
| Antisentido (antisense) | Hebra de ARN complementaria a un ARNm; bloquea su traducción |
| Archaea (Arqueas) | Dominio de procariotas distintos de las bacterias; comparten rasgos con eucariotas |
| ARN guía (crRNA/sgRNA) | ARN que dirige a Cas9 hacia la secuencia blanco en CRISPR |
| ARNm (mensajero) | ARN que lleva la información del gen para ser traducida en proteína |
| ARNr (ribosomal) | ARN estructural y catalítico que forma parte del ribosoma |
| ARNt (transferencia) | ARN adaptador que lleva aminoácidos al ribosoma según el código codón-anticodón |
| Bacteriófago (fago) | Virus que infecta bacterias |
| Cápsula 5′ (cap) | 7-metilguanilato unido al extremo 5′ del ARNm eucariota; necesaria para traducción |
| Cas9 | Endonucleasa del sistema CRISPR que corta ADN de doble hebra |
| Codón | Triplete de nucleótidos del ARNm que especifica un aminoácido o señal de término |
| Cola poli-A | Cadena de adeninas añadida al extremo 3′ del ARNm eucariota |
| CRISPR | Sistema inmune adaptativo de procariotas; herramienta de edición génica |
| DICER | RNasa III que procesa dsRNA o pre-miRNA en fragmentos de ~21 nt |
| DNAasa | Enzima que degrada ADN |
| dsRNA | ARN de doble hebra (*double-stranded RNA*) |
| Elongación | Fase de la traducción donde se añaden aminoácidos secuencialmente |
| Enhancer | Secuencia reguladora que potencia la transcripción de un gen |
| Epigenética | Regulación de la expresión génica sin cambio en la secuencia del ADN |
| Eucromatina | Cromatina descondensada, accesible para transcripción |
| Factor de liberación (RF) | Proteína que reconoce codones de término y libera la cadena polipeptídica |
| Factor de transcripción | Proteína reguladora que se une al ADN para controlar la transcripción |
| fMet (formil-metionina) | Primer aminoácido de proteínas bacterianas; metionina con grupo formilo |
| Footprinting | Técnica para identificar regiones del ADN protegidas por proteínas unidas |
| Heterocromatina | Cromatina condensada; genes silenciados/inaccesibles |
| Histona | Proteína básica alrededor de la cual se enrolla el ADN en nucleosomas |
| Iniciación | Fase de la traducción donde se ensambla el ribosoma sobre el ARNm en el codón de inicio |
| Intrón | Secuencia no codificante dentro de un gen; eliminada por splicing |
| Isla CpG | Región rica en dinucleótidos CG; sitio preferente de metilación |
| Knockdown | Reducción parcial de la expresión de un gen |
| Knockout | Eliminación completa de un gen o su función |
| Marco de lectura | Secuencia de codones consecutivos desde el codón de inicio hasta el de término |
| Metilación | Adición de un grupo metilo (-CH₃) a ADN o proteínas |
| miRNA | MicroARN endógeno codificado en el genoma que regula expresión génica |
| Mirtoma | Conjunto completo de miRNAs de un organismo o tipo celular |
| Nucleosoma | ADN enrollado alrededor de un octámero de histonas |
| Off-target | Efecto no deseado de CRISPR en un sitio diferente al blanco |
| Operón | Unidad de transcripción policistrónica en procariotas |
| PAM | Secuencia corta adyacente al protospaciador necesaria para el corte por Cas9 |
| Polisoma | Múltiples ribosomas traduciendo simultáneamente un ARNm |
| Promotor | Región del ADN donde se inicia la transcripción |
| Proteoma | Conjunto de proteínas expresadas en una condición dada |
| Puromicina | Antibiótico análogo de aminoacil-tRNA que termina prematuramente la traducción |
| Ribozima | ARN con capacidad catalítica (enzimática) |
| RISC | Complejo proteico efector de la interferencia de ARN |
| Shine-Dalgarno | Secuencia del ARNm bacteriano complementaria al rRNA 16S; guía la iniciación |
| siRNA | Small Interfering RNA exógeno o experimental que silencia genes |
| Sitios A, P, E | Sitios del ribosoma: aminoacil (entrada), peptidil (enlace peptídico), exit (salida) |
| Splicing | Proceso de eliminación de intrones y unión de exones en el ARNm |
| Terminación | Fase final de la traducción cuando un codón stop llega al sitio A |
| Titina | Proteína más grande conocida (~30.000 aa); componente del sarcómero muscular |
| Transcriptoma | Conjunto de ARNm expresados en una condición dada |
| Wobble (tambaleo) | Apareamiento flexible en la tercera posición del codón; permite que un tRNA reconozca más de un codón |

---

## 7. Notas administrativas

🎤 Clase —
- El profesor **subirá artículos** al aula virtual ("Carta" / plataforma del curso) para el seminario:
  - Revisiones de **epigenética** (incluyendo un número especial de *Investigación y Ciencia* en español).
  - Paper de **CRISPR** aplicado a ratones sordos.
  - Revisiones generales de regulación génica.
- **Seminario**: se harán presentaciones por parejas (2 personas por paper). El profesor asignará literatura pero los estudiantes también pueden proponer papers.
  - Preferencia: papers experimentales para quienes tengan más experiencia de laboratorio; revisiones (reviews) para quienes tengan menos experiencia.
  - Se sugirió que alguien presente un paper de **cáncer y epigenética**.
  - Se podría sacrificar un día de clases para dar más tiempo a las presentaciones.
- **Estefanía Astargo** (alumna): ausente por viaje a Brasil; el profesor le enviará la información.
- Recurso recomendado: **nobelprize.org** — discurso, video y resumen divulgativo de los premios Nobel relevantes (CRISPR 2020, ribozimas 1989, etc.).
- Los estudiantes con menos base en biología molecular deben comunicarse con el profesor para recibir material introductorio.

---

## Huecos del audio

Los siguientes fragmentos de la transcripción fueron ininteligibles o demasiado distorsionados para extraer contenido confiable:

1. **Línea 12, final**: "no sé si existe un problema del cable si también está un poco en el mismo lugar…" — fragmento repetitivo sin contenido académico claro; posible problema de conexión de un alumno remoto.
2. **Líneas 30–35**: conversación sobre dosímetros y radiación en contexto laboral (resonancia magnética, scanner). No es contenido central del curso pero sí ilustra la diferencia entre mutación por radiación (genómica) vs. epigenética.
3. **Líneas 42–44**: discusión logística sobre organización del seminario; fragmentada pero la información relevante está capturada en Notas administrativas.
4. **Líneas 58–64**: discusión técnica sobre gradientes de densidad, kits de purificación de miRNA, y secuenciación del mirtoma. Parcialmente recuperable; lo relevante está integrado en la sección 3.12.

---

## Puente Clase 1 → Clase 2

Esta sección conecta explícitamente los contenidos de la Clase 1 (La química de la vida) con la Clase 2 (Bases de biología molecular).

### De moléculas a información

- En **Clase 1** se estudió la estructura de los **nucleótidos** (azúcar + base nitrogenada + fosfato), los extremos 5′/3′ y el modelo de Watson y Crick. Esto en **Clase 2** es la base para entender el **código genético**: tripletes de nucleótidos (codones) que especifican aminoácidos. Sin conocer la estructura del nucleótido y la complementariedad de bases, no se puede comprender cómo funciona la traducción ni el apareamiento codón-anticodón.

### De enlaces a estabilidad y regulación

- Los **puentes de hidrógeno** y **fuerzas hidrofóbicas** (Clase 1) explican la estabilidad de la doble hélice y las interacciones ADN-proteína. En **Clase 2** esto se aplica directamente a: (a) cómo los **factores de transcripción** reconocen secuencias específicas del ADN (interacción en el surco mayor), (b) por qué la **heterocromatina** es inaccesible (empaquetamiento con histonas), y (c) cómo los **puentes de hidrógeno** entre codón y anticodón permiten la traducción.

### De aminoácidos y proteínas a la maquinaria celular

- La clasificación de **aminoácidos** (hidrófobos, cargados, polares) y los niveles de **estructura proteica** (Clase 1) son esenciales para entender en **Clase 2**: (a) por qué ciertas mutaciones missense son más dañinas que otras (cambiar un aa hidrófobo por uno cargado altera el plegamiento), (b) cómo funcionan las **enzimas** involucradas en la expresión génica (ARN polimerasa, aminoacil-tRNA sintetasas, Cas9, DICER), (c) qué son los **factores de transcripción** (proteínas con dominios de unión a ADN).

### De la enzimología a la catálisis ribosómica

- En **Clase 1** se estudiaron las enzimas como catalizadores que bajan la energía de activación sin alterar el equilibrio. En **Clase 2** se demuestra que **no solo las proteínas son enzimas**: el ribosoma (rRNA) cataliza el enlace peptídico como una ribozima. Esto conecta con la hipótesis del mundo de ARN.

### Del concepto de polímero al flujo de información

- La idea de **monómero → polímero** (Clase 1) se extiende en Clase 2 al concepto de **información codificada en secuencia**: la secuencia de nucleótidos en el ADN determina la secuencia de aminoácidos en la proteína. La capacidad de polimerizar en cualquier orden (Clase 1: "posibilidades casi infinitas de variedad") es lo que permite almacenar información genética.

### De la bicapa lipídica a la compartimentalización

- Los **fosfolípidos y la bicapa** (Clase 1) explican por qué existe la **compartimentalización celular** (Clase 2): la membrana nuclear separa transcripción de traducción en eucariotas. Sin entender la naturaleza anfipática de los fosfolípidos, no se puede comprender por qué la célula eucariota puede tener un núcleo.

### De la denaturación y priones a la regulación post-traduccional

- El concepto de **denaturación proteica y priones** (Clase 1) prepara la idea de **regulación post-traduccional** (Clase 2): las proteínas pueden ser degradadas, modificadas (fosforilación, acetilación, metilación de histonas) o cambiar de conformación para modular su función. La fosforilación de histonas (Clase 2 - epigenética) es una modificación post-traduccional que altera la expresión génica.

### Resumen del puente

| Concepto en Clase 1 | Cómo se aplica / profundiza en Clase 2 |
|---|---|
| Nucleótido (azúcar + base + fosfato) | Codón (3 nucleótidos), código genético, traducción |
| Extremos 5′ / 3′, síntesis 5′→3′ | Dirección de lectura del ARNm, marco de lectura |
| Complementariedad A-T, C-G | Codón-anticodón, ARN guía en CRISPR, hibridación de miRNA/siRNA |
| Puentes de hidrógeno | Estabilidad hélice, interacción ADN-proteína, apareamiento en ribosoma |
| Fuerzas hidrofóbicas / entropía | Plegamiento de factores de transcripción, interior del ribosoma |
| Aminoácidos (20, clasificación) | Código genético degenerado, mutaciones conservadas vs. missense |
| Estructura de proteínas (4 niveles) | Factores de transcripción, histonas, enzimas de regulación, Cas9 |
| Enlace peptídico | Formado por ribozima (rRNA), elongación en ribosoma |
| Enzimas y catálisis | Ribozima, aminoacil-tRNA sintetasa, DICER, Cas9 |
| Fosfolípidos / bicapa | Compartimentalización nuclear eucariota |
| Denaturación / modificaciones | Regulación post-traduccional, epigenética (modificaciones de histonas) |
| ATP como moneda energética | Hidrólisis de GTP en traducción (EF-Tu, EF-G, IF2) |

---

## Tabla resumen de artículos (Articulos_Clase2)

### CRISPR

| # | Título | Autores | Revista | Año | Tema central |
|---|--------|---------|---------|-----|--------------|
| 1 | CRISPR–Cas9 Structures and Mechanisms | Jiang F, Doudna JA | *Annu. Rev. Biophys.* | 2017 | Mecanismo estructural de Cas9: reconocimiento de PAM, formación del R-loop y corte de ADN |
| 2 | CRISPR/Cas, the Immune System of Bacteria and Archaea | Horvath P, Barrangou R | *Science* | 2010 | Revisión del sistema inmune adaptativo CRISPR/Cas en procariotas |
| 3 | Development and Applications of CRISPR-Cas9 for Genome Engineering | Hsu PD, Lander ES, Zhang F | *Cell* | 2014 | Desarrollo de CRISPR-Cas9 como plataforma de edición genómica en eucariotas |
| 4 | A Programmable Dual-RNA–Guided DNA Endonuclease in Adaptive Bacterial Immunity | Jinek M, Chylinski K, Fonfara I, Hauer M, Doudna JA, Charpentier E | *Science* | 2012 | Demostración de que Cas9 guiado por dual-RNA (o quimera) corta ADN de forma programable |
| 5 | Treatment of autosomal dominant hearing loss by in vivo delivery of genome editing agents | Gao X, Tao Y *et al.*, Liu DR, Chen Z-Y | *Nature* | 2017 | Edición alelo-específica con Cas9-RNP in vivo para tratar sordera dominante (modelo Tmc1 Bth) |

### Epigenética

| # | Título | Autores | Revista | Año | Tema central |
|---|--------|---------|---------|-----|--------------|
| 6 | Combining Epigenetic and Immune Therapy to Combat Cancer | Chiappinelli KB, Zahnow CA, Ahuja N, Baylin SB | *Cancer Research* | 2016 | Inhibidores de DNMT reactivan señalización inmune; combinación con inmunoterapia anti-cáncer |
| 7 | Epigenética: La herencia más allá de los genes (Especial) | Varios | *TEMAS / Investigación y Ciencia* | 2015 | Número especial de divulgación sobre epigenética, ambiente, cromatina, herencia y enfermedad |
| 8 | Advances in epigenetics link genetics to the environment and disease | Cavalli G, Heard E | *Nature* | 2019 | Revisión de epigenética: desarrollo, herencia transgeneracional, ambiente y enfermedad humana |
| 9 | A critical view on transgenerational epigenetic inheritance in humans | Horsthemke B | *Nature Communications* | 2018 | Análisis crítico de la evidencia de herencia epigenética transgeneracional en humanos |
| 10 | Metabolic regulation of pluripotency and germ cell fate through α-ketoglutarate | Tischler J, Gruhn WH *et al.*, Surani MA | *The EMBO Journal* | 2019 | α-cetoglutarato (ciclo TCA) regula enzimas epigenéticas que mantienen la pluripotencia y el destino germinal |

### Factores de transcripción

| # | Título | Autores | Revista | Año | Tema central |
|---|--------|---------|---------|-----|--------------|
| 11 | Identification and functional characterization of transcriptional activators in human cells | Alerasool N, Leng H, Lin Z-Y, Gingras A-C, Taipale M | *Molecular Cell* | 2022 | Screen basado en dCas9 identifica activadores transcripcionales humanos y sus dominios de activación |
| 12 | Potential roles of super enhancers in inflammatory gene transcription | Higashijima Y, Kanki Y | *The FEBS Journal* | 2021 | Super-enhancers como reguladores clave de la transcripción génica inflamatoria |
| 13 | Deciphering the multi-scale, quantitative cis-regulatory code | Kim S, Wysocka J | *Molecular Cell* | 2023 | Revisión integradora: factores de transcripción, elementos cis, cromatina y modelos cuantitativos |
| 14 | What do Transcription Factors Interact With? | Chen H, Pugh BF | *Journal of Molecular Biology* | 2021 | Interacciones de TFs con remodeladores de cromatina, GTFs, Mediator y Pol II para ensamblar PIC |

### Regulación a nivel de la traducción

| # | Título | Autores | Revista | Año | Tema central |
|---|--------|---------|---------|-----|--------------|
| 15 | Cell type-specific drug-inducible protein synthesis inhibition demonstrates that memory consolidation requires rapid neuronal translation | Shrestha P, Ayata P *et al.*, Klann E | *Nature Neuroscience* | 2020 | Inhibición quimiogenética célula-específica demuestra que la consolidación de memoria requiere traducción rápida en neuronas excitatorias |
| 16 | Elevated protein synthesis in microglia causes autism-like synaptic and behavioral aberrations | Xu Z-X, Kim GH *et al.*, Xu B | *Nature Communications* | 2020 | Sobre-traducción en microglía (vía eIF4E) produce fenotipo autista con sesgo masculino en ratones |
| 17 | Late Endosomes Act as mRNA Translation Platforms and Sustain Mitochondria in Axons | Cioni J-M, Lin JQ *et al.*, Holt CE | *Cell* | 2019 | Endosomas tardíos (Rab7a) sirven como plataformas de traducción local de mRNAs mitocondriales en axones |
| 18 | Protein Synthesis Initiation in Eukaryotic Cells | Merrick WC, Pavitt GD | *Cold Spring Harb. Perspect. Biol.* | 2018 | Revisión completa de la iniciación de traducción en eucariotas: cap, eIFs, reclutamiento de mRNA |
| 19 | Ribosome profiling reveals the what, when, where, and how of protein synthesis | Brar GA, Weissman JS | *Nat. Rev. Mol. Cell Biol.* | 2015 | Ribo-seq como herramienta para estudiar traducción a escala genómica: regulación, localización, ORFs alternativos |
| 20 | Aminoacyl-tRNA synthetases | Rubio Gomez MA, Ibba M | *RNA* | 2020 | Aminoacil-tRNA sintetasas: decodificación precisa, roles no traduccionales, enfermedad y expansión del código genético |
