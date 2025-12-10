---
license: apache-2.0
library_name: transformers
tags:
- text-generation
- finetuned
- instruct
- mistral
- mistral3
- 24b
- LoRA
- Saptiva AI
- KAL
- Mexico
- Spanish
- conversational
language:
- es
datasets:
- SaptivaAI/kal-mx-training-data
base_model: mistralai/Mistral-Small-3.2-24B-Instruct-2506
inference: true
---

# Large Language Model KAL-24B-mx-v1

## Descripción del Modelo 📜

KAL-24B-mx-v1 es un Large Language Model (LLM) basado en la arquitectura Mistral, entrenado y adaptado específicamente para el contexto del español de México. El modelo fue generado mediante un entrenamiento con adaptadores LoRA (Low-Rank Adaptation), los cuales han sido completamente fusionados con los pesos del modelo base. Como resultado, este es un modelo listo para inferencia directa, sin requerir la carga de adaptadores externos. Su propósito es responder en español neutro con adaptación mexicana, comprendiendo trámites, normatividad, cultura y lenguaje cotidiano mexicano.

**Desarrollado por:** Saptiva AI

**Modelo Base:** Mistral-Small-3.2-24B-Instruct-2506

**Identificador en Hugging Face:** SaptivaAI/KAL-24B-mx-v1

**Licencia:** Apache 2.0

**Idioma:** Español (México)

## Compatibilidad y Paridad con el Modelo Base

Este checkpoint es un **merge LoRA** sobre `mistralai/Mistral-Small-3.2-24B-Instruct-2506`.
- **Interfaz y uso**: idénticos al modelo base (Transformers/vLLM). Requiere `transformers>=4.57.1` y `mistral-common>=1.6.2`.
- **Validación del merge**: equivalencia 1:1 con el modelo `[base+LoRA]` mediante generación **greedy** y comparación por **IDs de tokens** en 8 prompts (PASS).

## Usos del Modelo

### Uso Directo

Este modelo está diseñado para uso inmediato sin necesidad de entrenamiento adicional.Para información dinámica (trámites gubernamentales, normativas actualizadas), se recomienda integrarlo con sistemas RAG (Retrieval-Augmented Generation) que proporcionen datos específicos y actuales para enriquecer las respuestas por caso de uso.

### Casos de Uso

1. **Asistencia Conversacional Avanzada (Chatbots):** Asistentes virtuales con comprensión profunda del lenguaje, capaces de resolver consultas complejas sobre trámites, servicios y aspectos culturales de México.

2. **Generación de Contenido Especializado:** Redacción de borradores, resúmenes y explicaciones sobre temas interrelacionados: normativas del SAT, funcionamiento de transferencias SPEI, interpretación de recibos de servicios.

3. **Sistemas de Pregunta-Respuesta (Q&A):** Soluciones que conectan información de múltiples fuentes para responder preguntas sobre procedimientos como obtención del CURP o requisitos de crédito Infonavit.

4. **Herramientas de Soporte para Trámites:** Aplicaciones que guían a usuarios a través de procedimientos complejos, anticipando dudas y proporcionando documentación relevante.

> **Nota Importante:** Como todo modelo de lenguaje, puede generar respuestas incorrectas. Verifique siempre la información crítica, especialmente en aplicaciones legales o financieras, antes de tomar decisiones.

### Usos Derivados (Downstream Use)

Al partir de una base que comprende profundamente el español y el contexto mexicano, los entrenamientos especializados (fine-tunings) son significativamente más rápidos, fáciles y económicos que entrenar desde modelos generalistas. El modelo puede especializarse aún más para dominios específicos, tales como:

- **Atención al Cliente Bancaria:** Chatbots especializados en servicios financieros mexicanos (SPEI, cuentas CLABE, tarjetas de crédito, inversiones CETES).

- **Asistencia Legal y Normativa:** Sistemas que interpretan leyes mexicanas, códigos civiles, regulaciones laborales y compliance.

- **Soporte Técnico en Telecomunicaciones:** Asistentes para ISPs y operadores móviles que explican planes, facturación y resolución de problemas técnicos.

- **Educación y Capacitación:** Tutores virtuales para contenido educativo mexicano, desde nivel básico hasta educación superior.

- **E-commerce y Retail:** Asistentes de ventas que manejan consultas sobre productos, envíos, devoluciones y promociones específicas del mercado mexicano.

## Sesgos, Riesgos y Limitaciones

### Usos Fuera de Alcance (Out-of-Scope Use)

Este modelo no está diseñado para:

- Sistemas en producción que requieran una precisión factual del 100% sin supervisión humana, especialmente en dominios legales, financieros o médicos.

- Generar contenido dañino, sesgado o inapropiado.

- Tomar decisiones críticas donde una alucinación del modelo pueda causar daño (ej. asesoría legal, diagnóstico médico).

- Casos de uso que requieran información en tiempo real sin proveer informacion via RAG u otros métodos. 

- Contextos fuera de México, ya que está optimizado para el español y la cultura de México.

### Limitaciones Conocidas

- **Corte de Conocimiento:** El conocimiento del modelo está limitado a sus datos de entrenamiento (fecha de corte: Septiembre 2025). No conoce eventos posteriores.

- **Especificidad de Dominio:** Su rendimiento puede disminuir en temas muy alejados de la normatividad, cultura de pagos y lenguaje coloquial de México.

- **Alucinaciones:** Como todos los LLMs, puede generar información que suena plausible pero es incorrecta. Verifique siempre los datos críticos.

- **Información Dinámica:** No puede acceder a actualizaciones en tiempo real de leyes, formularios o tarifas oficiales.

### Recomendaciones

- **Supervisión Humana:** Utilice siempre supervisión humana para aplicaciones críticas.

- **Verificación de la Información:** Verifique la información importante con fuentes fiables (sitios gubernamentales oficiales, profesionales certificados).

- **Uso de System Prompts:** Utilice system prompts detallados para guiar el comportamiento y el tono del modelo.

- **Integración con RAG para Datos Dinámicos:** Para información que cambia constantemente, integre el modelo con un sistema RAG para asegurar que las respuestas sean actuales.

## Detalles de Entrenamiento

### Fuentes del Modelo

- **Repositorio:** SaptivaAI/KAL-24B-mx-v1

- **Modelo Base:** mistralai/Mistral-Small-3.2-24B-Instruct-2506

- **Datasets de Entrenamiento:**
  - Corpus de Cultura y Lenguaje Mexicano
  - Corpus de Normatividad y Trámites Mexicanos

### Proceso de Entrenamiento

- **Base Model:** mistralai/Mistral-Small-3.2-24B-Instruct-2506

- **Technique:** LoRA (Low-Rank Adaptation) - Los adaptadores fueron posteriormente fusionados con el modelo base para crear la versión final.

- **Framework:** Hugging Face Transformers

- **Precision:** bfloat16

### Infraestructura de Entrenamiento

- **Hardware:** 8x NVIDIA H100 80GB GPUs

- **Training Time:**
  - Primera fase de entrenamiento: 12 horas
  - Segunda fase de entrenamiento: 12 horas
  - Total: 24 horas

## Evaluación

### Datos de Prueba, Factores y Métricas

El rendimiento del modelo se evalúa utilizando los siguientes factores:

**Benchmark de Contexto Mexicano (Interno):** Un dataset de evaluación con 200 ejemplos enfocados en el contexto mexicano, cubriendo:
- Normatividad y trámites (SAT, RFC, CURP, Infonavit, etc.)
- Cultura de pagos y servicios financieros
- Lenguaje coloquial y expresiones mexicanas
- Procedimientos gubernamentales

**Métricas de Evaluación:**
- **Accuracy:** Precisión en respuestas contra una referencia (ground-truth), con evaluación binaria (Correcto/Incorrecto).
- **Grounding Score:** Porcentaje de respuestas respaldadas por fuentes verificables (objetivo: ≥90%).
- **Perplexity:** Medida de confianza del modelo en sus predicciones.
- **Response Quality:** Evaluación cualitativa de claridad, completitud y adecuación cultural.

### Resultados

**Internal Benchmark Performance:**
- Accuracy en contexto mexicano: 80% en el benchmark interno
- Grounding score: 80% de respuestas con respaldo verificable


El modelo demuestra:

✅ **Especialización en contexto mexicano:** Comprensión profunda de normativas, trámites y lenguaje coloquial mexicano, significativamente superior a modelos generalistas. Se beneficia de las capacidades mejoradas de su modelo base para seguir instrucciones.

✅ **Eficiencia en fine-tuning:** Como base para entrenamientos derivados, reduce tiempo y costos comparado con partir de modelos generalistas.

✅ **Respuestas culturalmente apropiadas:** Manejo de sutilezas del español mexicano y referencias culturales específicas.

> **Nota:** Este modelo está optimizado para casos de uso específicos del contexto mexicano. Benchmarks estándar en inglés (GSM8K, MMLU, etc.) no reflejan adecuadamente su propósito y capacidades especializadas.

## Especificaciones Técnicas

### Arquitectura del Modelo

- **Base:** mistralai/Mistral-Small-3.2-24B-Instruct-2506

- **Tipo:** Transformer (Decoder-only).

- **Parámetros Totales:** ~24 mil millones (24B).

- **Longitud de Contexto:** 128,000 tokens (prompt + salida totales)

- **Tamaño del Vocabulario:** ≈161,000 tokens

### Infraestructura de Cómputo

- **Entrenamiento:** Entrenado en un clúster de 8x NVIDIA H100 80GB.

- **Inferencia:** Optimizado para el contexto mexicano.

- **Requisitos de Memoria:** Mínimo ~55 GB de VRAM (bf16). Para contextos largos, se recomienda 1x GPU de 80 GB (ej. A100/H100).

### Archivos y formato
Este checkpoint usa `safetensors` **shardeado** con `model.safetensors.index.json`.
Transformers y vLLM cargan automáticamente todos los shards; **no es necesario** combinarlos en un solo archivo.

## Cómo Usar

### Instalación

```bash
pip install "transformers>=4.57.1" "torch>=2.2" "accelerate>=1.0" "mistral-common>=1.6.2"
```

### Uso Básico (Transformers)

```python
from transformers import AutoTokenizer, Mistral3ForConditionalGeneration
import torch

MODEL_ID = "SaptivaAI/KAL-24B-mx-v1"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = Mistral3ForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,  # o torch.float16
    device_map="auto"
)

SYSTEM_PROMPT = (
    "Eres KAL, la IA más inteligente enfocado en el contexto de México y en el idioma español . "
    "Responde de forma clara, precisa y concisa, citando pasos accionables cuando aplique."
)

def chat(user_text, max_new_tokens=512, temperature=0.15, top_p=0.9):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_text},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, return_tensors="pt", add_generation_prompt=True
    ).to(model.device)

    with torch.no_grad():
        output = model.generate(
            inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    new_tokens = output[0, inputs.shape[-1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

# Ejemplo
print(chat("¿Cómo puedo obtener mi CURP por primera vez?"))
```

> **Nota importante:** El modelo soporta hasta 128,000 tokens (prompt + salida combinados). Ajusta `max_new_tokens` según el tamaño de tu prompt.

### Uso en Producción con vLLM (Recomendado)

#### Servidor

```bash
pip install -U "vllm>=0.9.1"

vllm serve SaptivaAI/KAL-24B-mx-v1 \
  --dtype bfloat16 \
  --tokenizer-mode mistral \
  --config-format mistral \
  --load-format mistral \
  --tool-call-parser mistral \
  --tensor-parallel-size 1
```

Para configuración con 2 GPUs, usa `--tensor-parallel-size 2`.

#### Cliente (API Compatible con OpenAI)

```python
from openai import OpenAI

client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1")

response = client.chat.completions.create(
    model="SaptivaAI/KAL-24B-mx-v1",
    messages=[
        {"role": "system", "content": ""Eres KAL, la IA más inteligente de México. Responde con precisión y brevedad."},
        {"role": "user", "content": "¿Qué necesito para tramitar mi RFC?"}
    ],
    temperature=0.15,
    max_tokens=512
)

print(response.choices[0].message.content)
```

## Ejemplos de Uso

### Ejemplo 1: Trámites Gubernamentales (CURP)

**Prompt:**
```
¿Cuáles son los requisitos para obtener mi CURP por primera vez?
```

**Respuesta:**
```
Para obtener tu CURP por primera vez, necesitas presentar:

1. Acta de nacimiento original (certificada)
2. Identificación oficial (INE/IFE, pasaporte o cartilla militar)
3. Comprobante de domicilio reciente (no mayor a 3 meses)

Puedes tramitarlo de dos formas:
• En línea: A través del portal oficial de RENAPO (gob.mx/curp)
• Presencial: En cualquier módulo del Registro Civil

El trámite es completamente gratuito. Si lo haces en línea, puedes imprimir tu CURP inmediatamente. Si es presencial, te lo entregan en el momento.

Nota: Si naciste en el extranjero, también necesitarás tu acta de nacimiento apostillada o legalizada.
```

### Ejemplo 2: Cultura de Pagos (SPEI)

**Prompt:**
```
¿Cómo funciona una transferencia SPEI y cuánto tarda?
```

**Respuesta:**
```
SPEI (Sistema de Pagos Electrónicos Interbancarios) es el sistema del Banco de México para transferencias entre bancos.

Características principales:
• Velocidad: La transferencia se completa en menos de 1 minuto, las 24 horas del día, los 365 días del año
• Costo: Varía por banco, pero generalmente es gratuito o de bajo costo (10-20 pesos)
• Requisito: Necesitas la CLABE interbancaria del destinatario (18 dígitos)
• Límite: Depende de tu banco; típicamente entre 8,000 y 500,000 pesos por transferencia

Cómo hacer una transferencia SPEI:
1. Ingresa a tu banca en línea o app móvil
2. Selecciona "Transferencia SPEI" o "Transferencia a otros bancos"
3. Ingresa la CLABE del destinatario
4. Indica el monto
5. Confirma con tu token o contraseña

El dinero llega en segundos al destinatario, sin importar qué banco tenga.
```

### Ejemplo 3: Servicios Financieros (CETES)

**Prompt:**
```
¿Qué son los CETES y cómo puedo invertir en ellos?
```

**Respuesta:**
```
Los CETES (Certificados de la Tesorería de la Federación) son instrumentos de inversión emitidos por el gobierno mexicano a través de Banxico.

Características:
• Riesgo: Muy bajo, respaldados por el gobierno federal
• Rendimiento: Variable, actualmente entre 10-11% anual
• Plazos: 28, 91, 182 y 364 días
• Monto mínimo: Desde 100 pesos en plataformas digitales

Cómo invertir:
1. Plataforma cetesdirecto.com (oficial del gobierno):
   • Regístrate con CURP, RFC y cuenta bancaria
   • Monto mínimo: 100 pesos
   • Sin comisiones
2. A través de tu banco o casa de bolsa:
   • Montos mínimos más altos
   • Pueden cobrar comisiones

Ventajas: Inversión segura, accesible y con rendimientos superiores a cuentas de ahorro tradicionales. Ideal para ahorro a corto plazo.

Nota: Los rendimientos son antes de impuestos (ISR se retiene automáticamente).
```

### Ejemplo 4: Normatividad Fiscal (SAT)

**Prompt:**
```
¿Cuáles son los primeros pasos para darme de alta en el SAT?
```

**Respuesta:**
```
Para darte de alta en el SAT como persona física, sigue estos pasos:

Requisitos previos:
1. Tener tu CURP a la mano
2. Correo electrónico personal
3. Identificación oficial vigente (INE/IFE o pasaporte)
4. Comprobante de domicilio reciente

Pasos:
1. Agenda tu cita:
   • Entra a citas.sat.gob.mx
   • Selecciona "Inscripción al RFC"
   • Elige fecha, hora y oficina
2. Asiste a tu cita con:
   • Identificación oficial original
   • Comprobante de domicilio original
   • Acta de nacimiento (opcional pero recomendado)
3. En la oficina:
   • Te tomarán fotografía y huella
   • Definirás tu régimen fiscal (honorarios, arrendamiento, etc.)
   • Te entregarán tu Constancia de Situación Fiscal
4. Después de tu alta:
   • Activa tu Buzón Tributario
   • Genera tu e.firma (firma electrónica) si la necesitas

El trámite es gratuito y obtienes tu RFC el mismo día.
```

### Ejemplo 5: Lenguaje Coloquial

**Prompt:**
```
¿Qué significa cuando alguien dice "está cañón" en México?
```

**Respuesta:**
```
"Está cañón" es una expresión coloquial mexicana que significa que algo es difícil, complicado o intenso.

Usos comunes:
• Dificultad: "El examen está cañón" = El examen está muy difícil
• Situación seria: "Está cañón lo que pasó" = Es una situación grave
• Impresionante: "Está cañón ese concierto" = Ese concierto está increíble

Variantes:
• "Está muy cañón" (más enfático)
• "Está recañón" (extremadamente difícil/impresionante)

Sinónimos mexicanos: "está difícil", "está grueso", "está pesado"

Es una expresión muy común en el lenguaje cotidiano mexicano, usada en contextos informales.
```

## Requisitos Técnicos

### Requisitos de VRAM

- **Pesos del modelo:** ~55 GB (bf16/fp16)

- **Single-GPU:** 1× A100/H100 80 GB (contextos ≤64k tokens)

- **Multi-GPU:** 2× GPUs de 80 GB con tensor parallelism para contextos completos (128k tokens)

### Dependencias Clave

- transformers >= 4.57.1
- torch >= 2.2
- accelerate >= 1.0
- mistral-common >= 1.6.2 (tokenizador Mistral 3.x)

### Parámetros Recomendados

- **Temperature:** 0.15 (óptimo para seguimiento de instrucciones)
- **Context window:** 128,000 tokens (prompt + salida combinados)
- **System prompt:** Siempre incluir para mejores resultados

## Troubleshooting

**Problema:** Error de tokenización o plantilla de chat.

✅ **Solución:** Verifica que mistral-common>=1.6.2 esté instalado:
```bash
python -c "import mistral_common; print(mistral_common.__version__)"
```

**Problema:** Respuestas genéricas o fuera de contexto mexicano.

✅ **Solución:** Asegúrate de incluir un system prompt que especifique el contexto mexicano.

**Problema:** Memoria insuficiente (OOM).

✅ **Solución:**
- Reduce `max_new_tokens` o el tamaño del prompt.
- Usa tensor parallelism con múltiples GPUs.

## Citación

Si usas este modelo en tu trabajo, por favor cítalo de la siguiente manera:

```bibtex
@misc{kal_24b_mx_v1_2025,
  title={KAL-24B-mx-v1: Un Large Language Model adaptado para el contexto del español de México},
  author={Saptiva AI},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/SaptivaAI/KAL-24B-mx-v1}}
}
```