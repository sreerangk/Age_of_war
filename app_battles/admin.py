from django.contrib import admin

from app_battles.models import Battle

# Register your models here.


# @admin.register(Battle)
# class BattleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'created_at')


@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'short_result')
    list_filter = ('created_at', 'user')
    search_fields = ('my_platoons', 'opponent_platoons', 'result', 'user__username')
    readonly_fields = ('created_at',)

    def short_result(self, obj):
        return (obj.result[:50] + '...') if len(obj.result) > 50 else obj.result
    short_result.short_description = 'Result'
