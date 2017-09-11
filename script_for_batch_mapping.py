# -*- coding: utf-8 -*-

import arcpy
import os


sample_mxd_path = arcpy.GetParameterAsText(0)  # ArcMap示例文档
input_shp_folder_path = arcpy.GetParameterAsText(1)  # 输入文件所在文件夹
output_location = arcpy.GetParameterAsText(2)  # 输出位置
output_file_type = arcpy.GetParameterAsText(3)  # 输出文件类型

# 遍历指定文件夹
for root, dirs, files in os.walk(input_shp_folder_path):
    # 获取输入的SHP所在的文件夹路径
    shp_folder_path = root

    for shp_file in files:
        if shp_file.split('.')[1] == 'shp':
            # 修改编码格式，防止中文乱码
            shp_file = shp_file.decode('gbk').encode('utf-8')
            
            # 获取输入的SHP文件名称
            shp_file_name = shp_file.split('.')[0]

            # 组合输出文件路径
            output_file_path = output_location + '\\' + shp_file_name + '.' + output_file_type

            # 获取样本MXD文档
            sample_mxd = arcpy.mapping.MapDocument(sample_mxd_path)

            # 获取样本图层
            sample_lyr = arcpy.mapping.ListLayers(sample_mxd)[0]

            # 替换数据源
            sample_lyr.replaceDataSource(shp_folder_path, "SHAPEFILE_WORKSPACE", shp_file_name)

            # 出图
            if output_file_type == 'EMF':
                arcpy.mapping.ExportToEMF(sample_mxd, output_file_path)
            elif output_file_type == 'EPS':
                arcpy.mapping.ExportToEPS(sample_mxd, output_file_path)
            elif output_file_type == 'AI':
                arcpy.mapping.ExportToAI(sample_mxd, output_file_path)
            elif output_file_type == 'PDF':
                arcpy.mapping.ExportToPDF(sample_mxd, output_file_path)
            elif output_file_type == 'SVG':
                arcpy.mapping.ExportToSVG(sample_mxd, output_file_path)
            elif output_file_type == 'BMP':
                arcpy.mapping.ExportToBMP(sample_mxd, output_file_path)
            elif output_file_type == 'JPEG':
                arcpy.mapping.ExportToJPEG(sample_mxd, output_file_path)
            elif output_file_type == 'PNG':
                arcpy.mapping.ExportToPNG(sample_mxd, output_file_path)
            elif output_file_type == 'TIFF':
                arcpy.mapping.ExportToTIFF(sample_mxd, output_file_path)
            elif output_file_type == 'GIF':
                arcpy.mapping.ExportToGIF(sample_mxd, output_file_path)

            del sample_mxd
