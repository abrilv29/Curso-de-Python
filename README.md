# Configuración de Python en Windows con VS Code

## 1. Instalar Python

1. Descarga el instalador desde [python.org/downloads](https://www.python.org/downloads/)
2. Ejecuta el instalador
3. **Importante**: Marca la casilla "Add Python to PATH"
4. Haz clic en "Install Now"
5. Verifica la instalación:
   ```powershell
   python --version
   py --version
   pip --version
   ```

## 2. Instalar Visual Studio Code

1. Descarga VS Code desde [code.visualstudio.com](https://code.visualstudio.com/)
2. Ejecuta el instalador y sigue los pasos predeterminados

## 3. Configurar VS Code para Python

1. Abre VS Code
2. Instala la extensión **Python** (busca "Python" en Extensiones, publicada por Microsoft)
3. Instala la extensión **Pylance** (se instala automáticamente con Python)

### 3.1 Seleccionar intérprete de Python

1. `Ctrl + Shift + P` > "Python: Select Interpreter"
2. Elige tu instalación de Python

### 3.2 Configuración recomendada (settings.json)

Abre `Ctrl + Shift + P` > "Preferences: Open User Settings (JSON)" y añade:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  "python.terminal.activateEnvironment": true,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
  },
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

### 3.3 Atajos de teclado útiles

| Acción | Atajo |
|--------|-------|
| Ejecutar archivo | `Ctrl + F5` |
| Depurar | `F5` |
| Terminal integrado | `Ctrl + ñ` |
| Paleta de comandos | `Ctrl + Shift + P` |
| Formatear documento | `Shift + Alt + F` |
| Ir a definición | `F12` |
| Ver problemas | `Ctrl + Shift + M` |

### 3.4 Depuración (Debug)

1. Crea `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Python: Current File",
         "type": "python",
         "request": "launch",
         "program": "${file}",
         "console": "integratedTerminal",
         "justMyCode": true
       }
     ]
   }
   ```
2. Pon puntos de interrupción (click en margen izquierdo)
3. Presiona `F5` para depurar

## 4. Crear y ejecutar tu primer script

1. Crea una carpeta para tu proyecto
2. Abre la carpeta en VS Code (`File > Open Folder`)
3. Crea un archivo `main.py`:
   ```python
   print("¡Hola, Python!")
   ```
4. Ejecuta el script:
   - Opción A: Click derecho en el archivo > "Run Python File in Terminal"
   - Opción B: `Ctrl + Shift + P` > "Python: Run Python File in Terminal"
   - Opción C: Terminal integrado (`Ctrl + ñ`) > `python main.py`

## 5. Extensiones recomendadas

| Extensión | Descripción |
|-----------|-------------|
| Python | Soporte principal para Python |
| Pylance | IntelliSense rápido y type checking |
| Python Indent | Auto-indentación correcta |
| autoDocstring | Genera docstrings automáticamente |
| Code Runner | Ejecuta código con un click |

## Configurar terminal en VS Code para reconocer python/pip

### Verificar en terminal integrado (`Ctrl + ñ`)

```powershell
# Verificar comandos disponibles
python --version
py --version
pip --version
where python
where pip
```

### Si no reconoce los comandos:

**Opción A: Reiniciar VS Code después de instalar Python**
- Cierra **completamente** VS Code (incluye procesos en background)
- Vuelve a abrirlo

**Opción B: Agregar Python al PATH manualmente**
1. `Win + R` > `sysdm.cpl` > Enter
2. Pestaña "Opciones avanzadas" > "Variables de entorno"
3. En "Variables del sistema" > buscar `Path` > Editar
4. Agregar rutas:
   ```
   C:\Users\TU_USUARIO\AppData\Local\Programs\Python\PythonXX\
   C:\Users\TU_USUARIO\AppData\Local\Programs\Python\PythonXX\Scripts\
   ```
5. Reiniciar VS Code

**Opción C: Usar `py` launcher (recomendado en Windows)**
```powershell
# py maneja versiones automáticamente
py -3.11 --version
py -m pip install modulo
py -m venv venv
```

### Configurar terminal predeterminado en VS Code

`Ctrl + Shift + P` > "Terminal: Select Default Profile" > **PowerShell** o **Command Prompt**

### Settings.json para terminal

```json
{
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.env.windows": {
    "PYTHONPATH": "${workspaceFolder}"
  },
  "python.terminal.activateEnvInCurrentTerminal": true
}
```

### Verificar que VS Code detecta Python

`Ctrl + Shift + P` > "Python: Select Interpreter" > debe mostrar tu instalación

---

## Solución de problemas comunes

- **Python no reconocido**: Reinstala Python marcando "Add to PATH" o añade manualmente a las variables de entorno (ver arriba)
- **Módulo no encontrado**: Ejecuta `pip install <modulo>` o `py -m pip install <modulo>`
- **Extensión no funciona**: Recarga VS Code (`Ctrl + Shift + P` > "Developer: Reload Window")