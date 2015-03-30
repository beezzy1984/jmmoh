
from tryton_synchronisation import SyncMixin, SyncMode
from trytond.pool import PoolMeta
__all__ = ['OccupationalGroup',]


class OccupationalGroup(SyncMixin):
    '''Occupational Group'''
    __name__ = 'gnuhealth.occupation'
    __metaclass__ = PoolMeta
    unique_id_column = 'code'
    sync_mode = SyncMode.none
