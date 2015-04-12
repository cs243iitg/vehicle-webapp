from django.contrib import admin
from vms.models import IITGUser,StudentVehicle, EmployeeVehicle , Guard, Gate, ParkingSlot, SuspiciousVehicle, ResidentLog, VisitorLog, TheftReport , VehiclePass, Place, BusTiming, OnDutyGuard
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User

class IITGUserInline(admin.StackedInline):
    model = IITGUser
    can_delete = False
    verbose_name_plural = 'user'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (IITGUserInline, )
    list_display=('username','first_name','last_name','is_superuser','is_staff','user_is_student','user_is_security')
    def user_is_student(self,x):    
        return x.user.is_student

    def user_is_security(self,x):
        return x.user.is_security


class StudentVehicleAdmin(admin.ModelAdmin):
    model = StudentVehicle
    list_display = ('name', 'roll_number', 'vehicle_registration_number')

class EmployeeVehicleAdmin(admin.ModelAdmin):
    model = EmployeeVehicle
    list_display = ('name', 'employee_no', 'vehicle_registration_number')  
    readonly_fields=['declaration',]  



class ParkingSlotAdmin(admin.ModelAdmin):
    model = ParkingSlot
    list_display = ('parking_area_name', 'total_slots', 'available_slots')

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



# class RouteAdminInline(admin.TabularInline):
#     model=Route
#     extra=1

class PlaceAdmin(admin.ModelAdmin):
    model=Place

class BusTimingAdmin(admin.ModelAdmin):
    model=BusTiming

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(IITGUser)
admin.site.register(StudentVehicle, StudentVehicleAdmin)
admin.site.register(EmployeeVehicle, EmployeeVehicleAdmin)
admin.site.register(Gate)
admin.site.register(ParkingSlot, ParkingSlotAdmin)
admin.site.register(SuspiciousVehicle, SuspiciousVehicleAdmin)
admin.site.register(ResidentLog, ResidentLogAdmin)
admin.site.register(VisitorLog, VisitorLogAdmin)
admin.site.register(VehiclePass, VehiclePassAdmin)
admin.site.register(Guard)
admin.site.register(TheftReport)
admin.site.register(Place, PlaceAdmin)
admin.site.register(BusTiming, BusTimingAdmin)
admin.site.register(OnDutyGuard)