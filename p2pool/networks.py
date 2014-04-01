from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    skatecoin=math.Object(
        PARENT=networks.nets['skatecoin'],
        SHARE_PERIOD=5, # seconds target spacing
        CHAIN_LENGTH=12*60*60//5, # shares
        REAL_CHAIN_LENGTH=12*60*60//5, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=50, # blocks
        IDENTIFIER='DDA1A1D3B2F68CDD'.decode('hex'),
        PREFIX='A2C3D4D541C11CAA'.decode('hex'),
        P2P_PORT=10663,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=10664,
        BOOTSTRAP_ADDRS='91.230.205.78 91.230.204.187'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name

