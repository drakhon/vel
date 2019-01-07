from vel.openai.baselines.common.vec_env import VecEnv

from .rollout import Trajectories, Transitions


class ReplayBuffer:
    """ Base class for a replay buffer """
    def __init__(self):
        pass

    def is_ready_for_sampling(self) -> bool:
        """ If buffer is ready for drawing samples from it (usually checks if there is enough data) """
        raise NotImplementedError

    def update(self, rollout, batch_info):
        """ Perform update of the internal state of the buffer - e.g. for the prioritized replay weights """
        raise NotImplementedError

    def sample_transitions(self, batch_size, batch_info) -> Transitions:
        """ Sample transitions from replay buffer """
        raise NotImplementedError

    def sample_trajectories(self, rollout_length, batch_info) -> Trajectories:
        """ Sample transitions from replay buffer """
        raise NotImplementedError

    def store_transition(self, frame, action, reward, done, extra_info=None):
        """ Store given transition in the backend """
        raise NotImplementedError


class ReplayBufferFactory:
    """ Create a replay buffer based on supplied environment """

    def instantiate(self, environment: VecEnv):
        raise NotImplementedError
