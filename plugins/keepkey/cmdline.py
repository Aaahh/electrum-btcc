from electrum_ltc.plugins import hook
from electrum_ltc.util import print_msg, raw_input
from .keepkey import KeepKeyPlugin
from ..hw_wallet import CmdLineHandler

class Plugin(KeepKeyPlugin):
    handler = CmdLineHandler()
    @hook
    def init_keystore(self, keystore):
        if not isinstance(keystore, self.keystore_class):
            return
        keystore.handler = self.handler
