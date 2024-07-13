
# Twitter Community Detection

Este repositorio contiene el código y los datos necesarios para la detección y análisis de comunidades en Twitter. Utiliza diversas herramientas y bibliotecas para el análisis de redes sociales y la visualización de datos.

## Contenido del repositorio

### Directorios

- **data/**: Carpeta que contiene los datos utilizados para el análisis.
- **gephi/**: Archivos y scripts para trabajar con Gephi, una herramienta de visualización de grafos.
- **images/**: Imágenes generadas durante el análisis.

### Archivos

- **comm_analysis_metrics_2.ipynb**: Este notebook contiene el análisis de métricas de las comunidades detectadas. Utiliza bibliotecas como NetworkX para calcular métricas como centralidad, modularidad y coeficiente de agrupamiento.
- **communities_analysis.ipynb**: Este notebook realiza un análisis detallado de las comunidades detectadas en la red de Twitter, incluyendo la visualización de las comunidades y la exploración de sus características.
- **gephi_grapgh.py**: Script en Python para exportar datos de la red a un formato compatible con Gephi, permitiendo la visualización y el análisis de la red en esta herramienta.
- **info_evolution.ipynb**: Este notebook analiza la evolución de la información en la red de Twitter a lo largo del tiempo, identificando cómo se propagan los mensajes y cómo cambian las comunidades.
- **transport.ipynb**: Este notebook analiza datos de transporte relacionados con la red de Twitter, explorando cómo los patrones de transporte pueden influir en la formación de comunidades.
- **transport_only_dates.ipynb**: Un análisis centrado únicamente en las fechas específicas de los datos de transporte, evaluando su impacto en la red de Twitter.
- **transport_only_dates_analysis.ipynb**: Un análisis adicional que profundiza en las fechas específicas de los datos de transporte y su relación con la red de Twitter.
- **tw_com_det.ipynb**: Este notebook contiene el código principal para la detección de comunidades en Twitter utilizando algoritmos de detección de comunidades y visualización de resultados.
- **tw_cd_env.yaml**: Archivo de entorno Conda para la instalación de las dependencias necesarias.

### Otros archivos

- **.gitignore**: Archivo para excluir archivos y carpetas no deseados del control de versiones.
- **README.md**: Archivo con información sobre el repositorio.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ignacioalbornoz/twitter_community_detection.git
   ```
2. Navegar al directorio del proyecto:
   ```bash
   cd twitter_community_detection
   ```
3. Crear el entorno con Conda usando el archivo `tw_cd_env.yaml`:
   ```bash
   conda env create -f tw_cd_env.yaml
   ```

## Uso

1. Activar el entorno Conda:
   ```bash
   conda activate twitter_community_detection
   ```
2. Ejecutar los notebooks Jupyter para realizar los análisis necesarios:
   - `comm_analysis_metrics_2.ipynb`
   - `communities_analysis.ipynb`
   - `info_evolution.ipynb`
   - `transport.ipynb`
   - `transport_only_dates.ipynb`
   - `transport_only_dates_analysis.ipynb`
   - `tw_com_det.ipynb`
3. Utilizar los scripts en `gephi/` para la visualización de grafos con Gephi:
   - Ejecutar `gephi_grapgh.py` para exportar los datos a un formato compatible con Gephi.

## Ejemplos de Resultados

### Detección de Comunidades
![Detección de Comunidades](https://github.com/ignacioalbornoz/twitter_community_detection/blob/main/images/community_detection.png?raw=true)

### Evolución de la Información
![Evolución de la Información](https://github.com/ignacioalbornoz/twitter_community_detection/blob/main/images/info_evolution.png?raw=true)

### Análisis de Transporte
![Análisis de Transporte](https://github.com/ignacioalbornoz/twitter_community_detection/blob/main/images/transport_analysis.png?raw=true)


