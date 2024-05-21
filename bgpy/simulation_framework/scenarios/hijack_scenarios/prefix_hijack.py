from bgpy.simulation_framework.scenarios.scenario import Scenario

class PrefixHijack(Scenario):
    def _get_announcements(self, *args, **kwargs):
        raise NotImplementedError("This method should be overridden in a subclass.")
