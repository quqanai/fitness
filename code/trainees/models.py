from tortoise import fields, Model


class Trainee(Model):
    id = fields.UUIDField(pk=True)  # noqa: A003
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'trainees'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
