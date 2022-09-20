from tortoise import fields, Model


class User(Model):
    id = fields.UUIDField(pk=True)  # noqa: A003
    email = fields.CharField(max_length=100, unique=True)
    hashed_password = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'users'
