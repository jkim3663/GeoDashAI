from gym.envs.registration import register

register(
    # unique identifier for the env `name-version`
    id="GeometryDash-v1",
    # path to the class for creating the env
    # Note: entry_point also accept a class as input (and not only a string)
    entry_point="geodashai.env:GeometryDash",
    # Max number of steps per episode, using a `TimeLimitWrapper`
    max_episode_steps=500,
)