MOBS=['skeleton','skeletonRed','skeletonBlue','destroyer']


JSON = {
    "mobs" : [
    {
        "name" : "skeleton", 
        "type" : "skeleton",
        "moveSpeed" : 5,
        "bulletSpeed" : 10,
        "bulletType" : "green",
        "hp" : 100,
        "textureSize" : (64,64),
        "cooldown": 200.
        
        
    }, 
    {
        "name" : "skeletonRed", 
        "type" : "skeleton",
        "moveSpeed" : 5,
        "bulletSpeed" : 10,
        "bulletType" : "orange",
        "cooldown": 200,
        "hp" : 100,
        "textureSize" : (64,64),
    }, 
    {
        "name" : "skeletonBlue",
        "type" : "skeleton", 
        "moveSpeed" : 5,
        "bulletSpeed" : 10,
        "bulletType" : "aqua",
        "cooldown": 200,
        "hp" : 100,
        "textureSize" : (64,64),
    },
    {
        "name" : "destroyer",
        "type" : "destroyer",
        "moveSpeed" : 5,
        "bulletSpeed" : 5,
        "bulletType" : "green",
        "cooldown": 200,
        "hp" : 100,
        "textureSize" : (64,64),
        
    },
    {
        "name" : "boss",
        "type" : "boss",
        "moveSpeed" : 2,
        "bulletSpeed" : 5,
        "bulletType" : "green",
        "cooldown": 20,
        "hp" : 1000,
        "textureSize" : (120,120),           
    }
    ]
}