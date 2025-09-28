from torch.distributed.elastic.rendezvous.c10d_rendezvous_backend import C10dRendezvousBackend
from torch.distributed.elastic.rendezvous.dynamic_rendezvous import DynamicRendezvousHandler
from torch.distributed import TCPStore
import threading

server_store = TCPStore("127.0.0.1", 29400, is_master=True)
c10backend = C10dRendezvousBackend(server_store, "run_0")
rdzv_handler = DynamicRendezvousHandler.from_backend(run_id="run_0", store=server_store, backend=c10backend, min_nodes=1, max_nodes=3)

# Keep the process alive indefinitely
threading.Event().wait()