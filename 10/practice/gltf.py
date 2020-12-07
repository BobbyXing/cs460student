import numpy as np
import base64


VERTICES = np.array([
            0.,0.,0., 1.,0.,0., 1.,1.,0., 0.,1.,0., 
            0.,0.,1., 1.,0.,1., 1.,1.,1., 0.,1.,1.], dtype=np.float32)
INDICES = np.array([
            3, 1, 0, 2, 1, 3,
            5, 1, 6, 1, 2, 6,
            5, 4, 1, 1, 4, 0,
            3, 6, 2, 3, 7, 6,
            5, 6, 4, 4, 6, 7,
            0, 4, 3, 4, 7, 3
            ], dtype=np.int16)

HOWMANY_V = 8
HOWMANY_I = 36
MAX_X = 1
MAX_Y = 1
MAX_Z = 1
MIN_X = 0
MIN_Y = 0
MIN_Z = 0
MAX = 7
MIN = 0

HOWMANYBYTES_V = VERTICES.nbytes
HOWMANYBYTES_I = INDICES.nbytes

B64_VERTICES = base64.b64encode(VERTICES)
B64_INDICES = base64.b64encode(INDICES)

gltf = {
    "asset": {
        "version": "2.0",
        "generator": "CS460 Magic Fingers"
    },

  "accessors": [
        {
            "bufferView": 0,
            "byteOffset": 0,
            "componentType": 5126,
            "count": HOWMANY_V,
            "type": "VEC3",
            "max": [MAX_X, MAX_Y, MAX_Z],
            "min": [MIN_X, MIN_Y, MIN_Z]
        },
        {
            "bufferView": 1,
            "byteOffset": 0,
            "componentType": 5123,
            "count": HOWMANY_I,
            "type": "SCALAR",
            "max": [MAX],
            "min": [MIN]
        }
    ], 

    "bufferViews": [
        {
            "buffer": 0,
            "byteOffset": 0,
            "byteLength": HOWMANYBYTES_V,
            "target": 34962
        },
        {
            "buffer": 1,
            "byteOffset": 0,
            "byteLength": HOWMANYBYTES_I,
            "target": 34963
        }
    ],
    
    "buffers": [
        {
            "uri": "data:application/octet-stream;base64,"+str(B64_VERTICES, 'utf-8'),
            "byteLength": HOWMANYBYTES_V
        },
        {
            "uri": "data:application/octet-stream;base64,"+str(B64_INDICES, 'utf-8'),
            "byteLength": HOWMANYBYTES_I
        }
    ],
  
    "meshes": [
        {
            "primitives": [{
                 "mode": 4,
                 "attributes": {
                     "POSITION": 0
                 },
                 "indices": 1
            }]
        }
    ],

    "nodes": [
        {
            "mesh": 0
        }
    ],

    "scenes": [
        {
            "nodes": [
                0
            ]
        }
    ],

    "scene": 0
}