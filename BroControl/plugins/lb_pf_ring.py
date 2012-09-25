# This plugin sets necessary environment variables to run Bro with
# PF_RING load balancing.

import BroControl.plugin
import BroControl.config

class LBPFRing(BroControl.plugin.Plugin):
    def __init__(self):
        super(LBPFRing, self).__init__(apiversion=1)

    def name(self):
        return "lb_pf_ring"

    def pluginVersion(self):
        return 1

    def init(self):
        for nn in self.nodes():
            if nn.type != "worker" or nn.lb_method != "pf_ring":
                continue

            clusterid = BroControl.config.Config.pfringclusterid;

            if clusterid != "0":
                cid = "PCAP_PF_RING_CLUSTER_ID=%s" % clusterid

                clustertype = BroControl.config.Config.pfringclustertype;

                if clustertype == "2tuple":
                    cpf = "PCAP_PF_RING_USE_CLUSTER_PER_FLOW_2_TUPLE=1"
                elif clustertype == "4tuple":
                    cpf = "PCAP_PF_RING_USE_CLUSTER_PER_FLOW_4_TUPLE=1"
                elif clustertype == "5tupletcp":
                    cpf = "PCAP_PF_RING_USE_CLUSTER_PER_FLOW_TCP_5_TUPLE=1"
                elif clustertype == "5tuple":
                    cpf = "PCAP_PF_RING_USE_CLUSTER_PER_FLOW_5_TUPLE=1"
                else:
                    cpf = "PCAP_PF_RING_USE_CLUSTER_PER_FLOW=1"

                nn.env_vars += [cid, cpf]

