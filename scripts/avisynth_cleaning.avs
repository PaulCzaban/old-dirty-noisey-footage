
SetMemoryMax(4096) 

Loadplugin("plugins/removegrain.dll")
LoadPlugin("plugins/removedirt.dll")
LoadPlugin("plugins/MVTools2.dll")
Import("plugins/03_RemoveDirtMC.avs")

source = ImageSource("E:\0_Source\%06d.png", 0,56019, fps=24).ConvertToYV12()

cleaned= RemoveDirtMC(source,35)

output = cleaned.ConvertToRGB32()

output.ImageWriter( "E:\1_Cleaned\%06d.png", 0, 56019, "png")