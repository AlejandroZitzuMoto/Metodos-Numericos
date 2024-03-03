from setuptools import setup

setup(
    name = "paqroots",
    version = "0.1",
    description = "En este paquete vendran funciones para encontrar las raices de polinomios",
    author = "José Alejandro Zitzumbo Montaño",
    author_email = "ja.zitzumbomontano@ugto.mx",
    url = "",
    install_requires = [numpy], # añade cualquier paquete adicional que debe ser
                         # instalado una vez que se instale el paquete
    keywords = ['roots_python', 'primer paquete'],
    packages = ['Raiz', 'Raiz.comandos', 'Raiz.Raices.biseccion', 'Raiz.Raices.punto_fijo', 'Raiz.Raices.Newton', 'Raiz.Raices.secante1', 'Raiz.Raices.secante2'],  # estructura
    scripts = []
)