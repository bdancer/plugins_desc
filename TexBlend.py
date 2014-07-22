{
    "Desciption": "",
    "ID": "TexBlend",
    "Name": "Blend",
    "Parameters": [
        {
            "attr": "color_a",
            "default": [
                0.0,
                0.0,
                0.0
            ],
            "desc": "",
            "type": "TEXTURE"
        },
        {
            "attr": "color_b",
            "default": [
                0.0,
                0.0,
                0.0
            ],
            "desc": "",
            "type": "TEXTURE"
        },
        {
            "attr": "blend_amount",
            "default": 1.0,
            "desc": "",
            "type": "FLOAT_TEXTURE",
            "ui": {
                "max": 1048576,
                "min": -1048576,
                "soft_max": 64,
                "soft_min": 0
            }
        },
        {
            "attr": "composite",
            "default": false,
            "desc": "If true, color_b will be composited over color_a with the given weight, taking its alpha into account",
            "type": "BOOL"
        }
    ],
    "Type": "TEXTURE",
    "Widget": {
        "widgets": []
    }
}