from django.contrib import admin
from vms.models import StudentVehicle, FacultyVehicle , Guard, Gate, ParkingSlot, SuspiciousVehicle, ResidentLog, VisitorLog, TheftReport , VehiclePass, Route, Place, BusTiming

class StudentVehicleAdmin(admin.ModelAdmin):
    model = StudentVehicle
    list_display = ('name', 'roll_number', 'vehicle_registration_number')

class FacultyVehicleAdmin(admin.ModelAdmin):
    model = FacultyVehicle
    list_display = ('name', 'employee_no', 'vehicle_registration_number')    

class GateAdmin(admin.ModelAdmin):
    model = Gate
    list_display = ('gate_name', 'security_on_duty')

class ParkingSlotAdmin(admin.ModelAdmin):
    model = ParkingSlot
    list_display = ('parking_area_name', 'total_slots', 'available_slots', 'security_on_duty')

class SuspiciousVehicleAdmin(admin.ModelAdmin):
    model = SuspiciousVehicle
    list_display = ('vehicle_number', 'vehicle_type', 'vehicle_model')

class ResidentLogAdmin(admin.ModelAdmin):
    model = ResidentLog
    list_display = ('registration_number', 'gate', 'is_entering')

class VisitorLogAdmin(admin.ModelAdmin):
    model = VisitorLog
    list_display = ('vehicle_number', 'vehicle_model', 'in_time', 'out_time', 'in_gate', 'out_gate')

class VehiclePassAdmin(admin.ModelAdmin):
    model = VehiclePass
    list_display = ('vehicle_no','pass_number' , 'issue_date' , 'expiry_date')    

class RouteAdminInline(admin.TabularInline):
    model=Route
    extra=1

class PlaceAdmin(admin.ModelAdmin):
    model=Place

class BusTimingAdmin(admin.ModelAdmin):
    inlines= [RouteAdminInline,]

admin.site.register(StudentVehicle, StudentVehicleAdmin)
admin.site.register(FacultyVehicle, FacultyVehicleAdmin)
admin.site.register(Gate, GateAdmin)
admin.site.register(ParkingSlot, ParkingSlotAdmin)
admin.site.register(SuspiciousVehicle, SuspiciousVehicleAdmin)
admin.site.register(ResidentLog, ResidentLogAdmin)
admin.site.register(VisitorLog, VisitorLogAdmin)
admin.site.register(VehiclePass, VehiclePassAdmin)
admin.site.register(Guard)
admin.site.register(TheftReport)
admin.site.register(Route)
admin.site.register(Place, PlaceAdmin)
admin.site.register(BusTiming, BusTimingAdmin)