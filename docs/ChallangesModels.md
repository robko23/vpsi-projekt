# Challenge Models Documentation

## Challenge Model

The `Challenge` model represents a challenge that users can participate in.

### Fields:

- `title` (`CharField`): The title of the challenge (max length: 60, unique).
- `description` (`TextField`): A detailed description of the challenge.
- `metric` (`CharField`): The metric used to measure progress (max length: 30).
- `start` (`CharField`): The start date/time of the challenge (max length: 60).
- `end` (`CharField`): The end date/time of the challenge (max length: 60).
- `category` (`CharField`): The category to which the challenge belongs (max length: 30).
- `creator` (`ForeignKey` to `User`): The user who created the challenge. Deletion is protected. Defaults to user with ID 1.
- `created_at` (`DateTimeField`): The timestamp when the challenge was created (auto-generated).


## UserChallenge Model
The `UserChallenge` model represents a user's participation in a challenge.

### Fields:
- `challenge` (`ForeignKey` to `Challenge`): The challenge the user is participating in. Deletion is protected.
- `result` (`CharField`): The user's recorded result (max length: 30).
- `comment` (`TextField`, optional): Additional comments from the user.
- `user` (`ForeignKey` to `User`): The user participating in the challenge. Deletion is protected.
- `date` (`DateTimeField`): The timestamp when the user submitted their result (auto-generated).


## Relationships
- A `Challenge` can have multiple `UserChallenge` entries through the `user_challenges` related name.
- A `User` can participate in multiple challenges through the `user_challenges` related name.
