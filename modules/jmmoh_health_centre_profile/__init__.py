from trytond.pool import Pool
# from .celerytools import *
from .sync_models import OccupationalGroup


def register():
    Pool.register(
        OccupationalGroup,
        module='jmmoh_health_centre_profile', type_='model')
