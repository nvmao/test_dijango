from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from contextvars import ContextVar
import django.conf as conf

from constance import config

class MaosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maos'
    def ready(self):
        print("mao ...........")

        self.register_field("mao",12)
        self.register_field("mao",15)
        self.register_site_field("/maos","mao2",33)
        self.register_site_field("/maos","mao3",35)
        self.register_site_field("/about","mao",34)

        # print(conf.settings.CONSTANCE_CONFIG['HELLO'])

        pass # startup code here

    
    
    def register_field(self, FILD_NAME,default_value=0,label=_("Brand attribute"),field_type=int):
        conf.settings.CONSTANCE_CONFIG['M_DEFAULT'] = ( ContextVar(FILD_NAME, default=default_value),label,field_type)

        # print(conf.settings.CONSTANCE_CONFIG['M_DEFAULT'])

        pass


    def register_site_field(self,site,FILD_NAME,default_value=0,label=_("Brand attribute"),field_type=int):
        conf.settings.CONSTANCE_CONFIG[site] = ( ContextVar(FILD_NAME, default=default_value),label,field_type)
        # print(conf.settings.CONSTANCE_CONFIG[site])


        pass
