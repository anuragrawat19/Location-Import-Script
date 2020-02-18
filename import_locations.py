import xlrd
from masterdata.models import (Boundary,BoundaryLevel)

def location_info(level_name,obj_name,parent=None):
    obj_code = BoundaryLevel.objects.get(name__iexact = level_name)
    obj,created = Boundary.objects.get_or_create(name__iexact = obj_name, boundary_level_type = obj_code,parent = parent)
    if created:
        obj.name = obj_name
        obj.save()
    return obj


def import_location(path):
    workbook = xlrd.open_workbook(path)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):
        state_name = str(sheet.cell(row_idx, 0).value).encode('utf-8').strip()
        level_name1 = "state"
        parent,created = Boundary.objects.get_or_create(name__iexact = "India")
        stateobj = location_info(level_name1,state_name,parent)
        district_name = str(sheet.cell(row_idx, 1).value).encode('utf-8').strip()
        level_name2 = "district"
        if stateobj:
            districtobj = location_info(level_name2,district_name,stateobj)
            print ("district",districtobj)
            area_name = str(sheet.cell(row_idx, 2).value).encode('utf-8').strip()
            level_name3 = "area"
            areaobj = location_info(level_name3,area_name,districtobj)
            print ("area",areaobj)
            mandal_name = str(sheet.cell(row_idx, 3).value).encode('utf-8').strip()
            level_name4 = "mandal"
            mandalobj = location_info(level_name4,mandal_name,areaobj)
            print ("mandal",mandalobj)
            village_name = str(sheet.cell(row_idx, 4).value).encode('utf-8').strip()
            level_name5 = "village"
            villageobj = location_info(level_name5,village_name,mandalobj)
            print ("village",villageobj)
            community_name = str(sheet.cell(row_idx, 5).value).encode('utf-8').strip()
            level_name6 = "community"
            communityobj = location_info(level_name6,community_name,villageobj)
            print ("community",communityobj)
        else:
            break


def import_poshan_location(path):
    workbook = xlrd.open_workbook(path)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):
        state_name = str(sheet.cell(row_idx, 0).value).encode('utf-8').strip()
        level_name1 = "State"
        parent,created = Boundary.objects.get_or_create(name__iexact = "India")
        stateobj = location_info(level_name1,state_name,parent)
        stateobj.code = str(sheet.cell(row_idx, 1).value).encode('utf-8').strip()
        stateobj.save()
        district_name = str(sheet.cell(row_idx, 2).value).encode('utf-8').strip()
        level_name2 = "District"
        district_code = str(sheet.cell(row_idx, 3).value).encode('utf-8').strip()
        if stateobj:
            districtobj = location_info(level_name2,district_name,stateobj)
            districtobj.code = str(sheet.cell(row_idx, 4).value).encode('utf-8').strip()
            districtobj.save()
            print ("district",districtobj,districtobj.code)
            area_name = str(sheet.cell(row_idx, 4).value).encode('utf-8').strip()
            level_name3 = "Block"
            areaobj = location_info(level_name3,area_name,districtobj)
            areaobj.code = str(sheet.cell(row_idx, 5).value).encode('utf-8').strip()
            areaobj.save()
            print ("block",areaobj,areaobj.code)
            mandal_name = str(sheet.cell(row_idx, 6).value).encode('utf-8').strip()
            level_name4 = "Sector"
            mandalobj = location_info(level_name4,mandal_name,areaobj)
            mandalobj.code = str(sheet.cell(row_idx, 7).value).encode('utf-8').strip()
            mandalobj.save()
            print ("sector",mandalobj,mandalobj.code)
            village_name = str(sheet.cell(row_idx, 8).value).encode('utf-8').strip()
            level_name5 = "Anganwadi"
            villageobj = location_info(level_name5,village_name,mandalobj)
            villageobj.code = str(sheet.cell(row_idx, 9).value).encode('utf-8').strip()
            villageobj.save()
            print ("Anganwadi",villageobj,villageobj.code)
#            community_name = str(sheet.cell(row_idx, 5).value).encode('utf-8').strip()
#            level_name6 = "community"
#            communityobj = location_info(level_name6,community_name,villageobj)
#            print ("community",communityobj)
        else:
            break

def import_location_akrspi(path):
    workbook = xlrd.open_workbook(path)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):
        state_name = str(sheet.cell(row_idx, 0).value).encode('utf-8').strip()
        level_name1 = "State"
        stateobj = location_info(level_name1,state_name)
        region_name = str(sheet.cell(row_idx, 1).value).encode('utf-8').strip()
        level_name2 = "Region"
        if stateobj:
            regionobj= location_info(level_name2,region_name,stateobj)
            print ("Region",regionobj)
            district_name = str(sheet.cell(row_idx, 2).value).encode('utf-8').strip()
            level_name3 = "District"
            districtobj = location_info(level_name3,district_name,regionobj)
            print ("district",districtobj)
            cluster_name = str(sheet.cell(row_idx, 3).value).encode('utf-8').strip()
            level_name4 = "Cluster"
            clusterobj = location_info(level_name4,cluster_name,districtobj)
            print ("cluster",clusterobj)
            block_name = str(sheet.cell(row_idx, 4).value).encode('utf-8').strip()
            level_name5 = "Block"
            blockobj = location_info(level_name5,block_name,clusterobj)
            print ("block",blockobj)
            
            gp_name = str(sheet.cell(row_idx, 5).value).encode('utf-8').strip()
            level_name6 = "GramPanchayat"
            gpobj = location_info(level_name6,gp_name,blockobj)
            print ("gramPanchayat",gpobj)
            
            village_name = str(sheet.cell(row_idx, 6).value).encode('utf-8').strip()
            level_name7 = "Village"
            villageobj = location_info(level_name7,village_name,gpobj)
            print ("Village",villageobj)
            
            hamlet_name = str(sheet.cell(row_idx, 7).value).encode('utf-8').strip()
            level_name8 = "Hamlet"
            hamletobj = location_info(level_name8,hamlet_name,villageobj)
            print ("hamlet",hamletobj)
        else:
            break



