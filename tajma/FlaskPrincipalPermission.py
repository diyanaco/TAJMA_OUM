from flask_principal import Permission, RoleNeed
from tajma.constants import RoleEnum

user_permission = Permission(RoleNeed(RoleEnum.STUDENT.value),
                             RoleNeed(RoleEnum.ADMIN.value),
                             RoleNeed(RoleEnum.SUPER_ADMIN.value))

admin_permission = Permission(RoleNeed(RoleEnum.ADMIN.value))

student_permission = Permission(RoleNeed(RoleEnum.STUDENT.value))