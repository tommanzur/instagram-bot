import random

def generate_image_prompt():
    '''Genera un nombre de imagen y un prompt sin incluir texto en las imágenes generadas.'''

    elements = [
        "personajes con implantes cibernéticos visibles",
        "vehículos flotantes en un horizonte urbano nocturno",
        "motos de alta velocidad con luces de neón",
        "ciudades futuristas con rascacielos iluminados por hologramas",
        "escenas de mercado callejero con tecnología avanzada y artefactos cibernéticos",
        "armas futuristas y equipamiento táctico en un entorno urbano degradado",
        "interacciones entre humanos y androides en espacios públicos abarrotados",
        "paisajes urbanos con publicidad masiva proyectada en el aire",
        "estaciones de metro subterráneas iluminadas con luces tenues y pantallas digitales",
        "robots de servicio realizando tareas cotidianas junto a humanos",
        "jardines verticales integrados en estructuras de edificios altos",
        "personajes usando realidad aumentada en interacciones cotidianas",
        "vehículos aéreos personales navegando entre los edificios",
        "distritos de entretenimiento donde la realidad virtual se mezcla con la física",
        "manifestaciones contra corporaciones poderosas con carteles holográficos",
        "redes de datos visibles fluyendo en el aire, accesibles mediante dispositivos portátiles",
        "talleres clandestinos de modificación corporal con tecnología avanzada",
        "policías con armaduras exoesqueléticas patrullando las calles",
        "ambientes subterráneos habitados por comunidades marginales",
        "infraestructura de la ciudad con cables y tuberías expuestos, cubiertos de neón",
        "edificios antiguos contrastando con nuevos rascacielos de tecnología punta",
        "lugares abandonados reutilizados por hackers y artistas",
        "andenes de tren elevados que atraviesan la ciudad entre rascacielos",
        "zonas de la ciudad controladas por IA con seguridad automatizada",
        "graffitis digitales proyectados en paredes que cambian dinámicamente",
        "mercados negros de información y tecnología bajo el radar",
        "siluetas de drones de vigilancia cruzando el cielo nocturno",
        "escenarios de revueltas urbanas con uso de tecnología disruptiva",
        "parques tecnológicos donde la naturaleza se fusiona con lo artificial"
    ]

    selected_elements = random.sample(elements, k=3)
    prompt = f"""Imagina una escena cyberpunk visualmente rica que incluya {selected_elements[0]}.
    Captura la esencia de un futuro distópico donde la tecnología y la humanidad 
    se entrelazan de maneras complejas, sin incluir ningún texto visible en la imagen."""
    image_name = f"cyberpunk_scene_{random.randint(100, 999)}"

    return (image_name, prompt)
