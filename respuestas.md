1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica
cómo se soluciona si hiciste push, y cómo si aún no hiciste.

De ser posible, que quede solo un commit con los cambios

si ya se hizo el push del commit se puede hacer los siguientes pasos:
1) Agregar el archivo con git add <nombre_archivo>.
2) Ejecutar el comando git commit --amend --no-edit para agregar el archivo al último commit sin cambiar el mensaje.
3) Ejecutar el comando git push --force-with-lease origin para enviar los cambios al repositorio remoto.

Es importante tener cuidado con este último comando, ya que puede sobrescribir los cambios realizados
por otros usuarios en el repositorio remoto.

si aún no se ha hecho el push del commit se puede seguir estos pasos:

1) Agrega el archivo git add <archivo>.
2) git commit --amend --no-edit para agregar el archivo al último commit sin cambiar el mensaje del commit.



2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has
trabajado?

A lo largo de mi carrera, he tenido la oportunidad de trabajar con una amplia gama de flujos de trabajo en el control de versiones.
Estos van desde el enfoque básico del flujo de trabajo centralizado hasta el uso de solicitudes de extracción (pull requests),
e incluso hasta la implementación de despliegues automáticos tras la aprobación de dichas solicitudes.

Actualmente, en la empresa en la que me encuentro, estamos utilizando el flujo de trabajo basado en ramas de funciones.
Para poder incorporar los cambios a la rama principal, es necesario solicitar una solicitud de extracción. Una vez que
se verifica y aprueba la solicitud, los cambios se fusionan en la rama principal. Posteriormente, se despliegan automáticamente
en el servidor. Este proceso asegura la calidad del código y facilita
la integración continua y la entrega continua (CI/CD).

3. ¿Cuál ha sido la situación más compleja que has tenido con esto?

Uno de los desafíos más complejos que he enfrentado ocurrió cuando compartíamos repositorios con una empresa aliada.
Esta empresa no seguía un enfoque de trabajo ordenado; no trabajaban en su propia rama,
no seguían los patrones que habíamos diseñado para el código, y mucho menos para la estructura del proyecto.

Esto resultó en varias ocasiones en que el proyecto se retrasó debido a que sus cambios causaban problemas en el código.
En términos coloquiales, “rompían producción” con frecuencia.

Al darnos cuenta de estos problemas, tuvimos que mejorar nuestros procesos y llegar a un acuerdo con el equipo para adoptar
una metodología de trabajo unificada. Una de las soluciones implementadas fue la introducción de las solicitudes de extracción
(pull requests) para revisar y aprobar los cambios antes de fusionarlos en la rama principal. A pesar de que ellos argumentaban
que nuestros procesos ralentizaban el proyecto, era crucial encontrar un equilibrio que permitiera a todos trabajar de manera eficiente
y efectiva. El objetivo final era, por supuesto, avanzar con el proyecto de manera oportuna y ordenada.

4. ¿Qué experiencia has tenido con los microservicios?

Aunque mi experiencia laboral con microservicios ha sido limitada, 
he tenido la oportunidad de trabajar con AWS Lambda con este propósito en el ámbito profesional.
En mi tiempo libre, me dedico a la autoformación y experimentación con tecnologías emergentes en este campo. 
Actualmente, estoy explorando Docker y Kubernetes, centrándome en entender su funcionamiento y cómo se orquestan 
los servicios con estas herramientas. Continúo esforzándome por ampliar mis conocimientos y habilidades en esta área.

5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?
En cuanto a mi preferencia entre los servicios en la nube de Google Cloud Platform (GCP) y Amazon Web Services (AWS), 
me inclino hacia AWS. Esta preferencia se basa en mi experiencia personal, ya que he 
trabajado con una mayor variedad de servicios en AWS , incluyendo EC2, AWS Lambda, entre otros. Considero que 
AWS es un sistema confiable que permite escalar o adaptar sus soluciones a las necesidades específicas
de cada proyecto sin dificultades.