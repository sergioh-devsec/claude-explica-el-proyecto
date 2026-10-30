# Cuenta el proyecto

Soy Serch, de CyberSerchMX. Quiero que otra persona entienda por qué hice una herramienta, cómo probarla y dónde deja de servir.

Este proyecto forma parte de mi práctica como ingeniero en diseño de software y redes y entusiasta de la ciberseguridad. Estoy reuniendo ejercicios que ya tenía y utilidades nuevas en repositorios pequeños, con un objetivo concreto y límites visibles. No presento esta muestra como un trabajo contratado ni como un resultado de clientes.

## Para qué lo uso
Preparé una definición de subagente de Claude Code con acceso de lectura. Lee estructura, puntos de entrada y pruebas. Produce un borrador de README con propósito, requisitos, comandos realmente existentes, ejemplo, límites y próximos pasos. Escribe en primera persona solo a partir de motivaciones aportadas; no inventes experiencias, clientes, fechas ni pruebas ejecutadas.

## Cómo probarlo
Requiere Claude Code y una cuenta/configuración propia. Copia el archivo de .claude/agents/ al mismo directorio de tu proyecto. Abre una nueva sesión y solicita explícitamente el agente por su nombre. Prueba primero examples/caso.md.

Validación: python tests/check.py

[Formato oficial](https://code.claude.com/docs/en/sub-agents).

## Qué revisé al construirlo
Separé la lógica de la interfaz o de la entrada de archivos para probar los casos de error. Mi enfoque de seguridad es reducir permisos y dependencias, validar datos antes de trabajar con ellos y no prometer más de lo que el código hace.

**Nivel:** Intermedio. Las pruebas incluidas son reproducibles; no equivalen a una auditoría independiente.

## Límites y siguiente paso
Es una configuración, no un modelo ni un servicio autónomo. No incluye cuentas ni créditos. Validé la estructura; no ejecuté una evaluación del modelo desde este repositorio. La calidad varía con el modelo y el contexto. Siguiente paso: registrar falsos positivos con datos ficticios.

No incluyas credenciales ni datos reservados en incidencias públicas. El repositorio no incorpora analítica. Código publicado para consulta; no se concede una licencia adicional de reutilización.

— Serch · [CyberSerchMX](https://github.com/sergioh-devsec)
