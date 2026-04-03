layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer-31": 43
        }
    },
    "layer-12": 35
}

# In giá trị layer-12
print("layer-12:", layers["layer-12"])

# In giá trị layer-31
print("layer-31:", layers["layer-11"]["layer-22"]["layer-31"])