# Entorno de Compilación LaTeX para el TFI

Para que el proyecto compile correctamente y los diagramas SVG se rendericen en el PDF, sigan estos pasos antes de empezar:

### 1. Instalar las dependencias del sistema
Abran **PowerShell como Administrador** y ejecuten estos tres comandos uno por uno (pueden tardar unos minutos):

* **Motor LaTeX (MiKTeX):**
  `winget install -e --id MiKTeX.MiKTeX --accept-source-agreements --accept-package-agreements`

* **Perl (Para que funcione la automatización de latexmk):**
  `winget install -e --id StrawberryPerl.StrawberryPerl --accept-source-agreements --accept-package-agreements`

* **Inkscape (Necesario para exportar los diagramas y circuitos .svg a PDF):**
  `winget install -e --id Inkscape.Inkscape --accept-source-agreements --accept-package-agreements`

### 2. Configuración de VS Code
* Vayan a la pestaña de extensiones de VS Code e instalen **LaTeX Workshop**.

### 3. Sincronización y Reinicio (¡Muy importante!)
1. Abran **MiKTeX Console** desde el menú de inicio de Windows.
2. Vayan a la pestaña **Updates** y hagan clic en "Check for updates" y luego en "Update now".
3. **Reinicie la computadora** (o cierren por completo VS Code y PowerShell) para que Windows detecte todas las rutas nuevas.

Al abrir este repositorio en VS Code, la configuración de compilado ya viene incluida. Solo abran `main.tex`, presionen `Ctrl + S`, y el PDF debería generarse solo.