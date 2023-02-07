from network import Network

net = Network({
    "Comida": ["Tifodea"],
    "Tifodea": ["Reacciones", "Fiebre", "Dolor"],
    "Gripe": ["Fiebre", "Dolor"]
})
