# portfolio, Justin Kapacinskas

See live site here: [https://justinkapacinskas.com](https://justinkapacinskas.com)

### to test backend locally

```bash
➜  python manage.py runserver

➜  curl -X POST http://localhost:8000/contact/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Cosmic Tester", "email": "alien@example.com", "message": "I come in peace!"}'
```

#### result

```javascript
{
     "message": "Contact saved successfully",
     "contact_id": 3
}
```

```sql
select *
from contact_contact;
```

| id  | name          | email             | message          | created_at                 |
| --- | ------------- | ----------------- | ---------------- | -------------------------- |
| 1   | Cosmic Tester | alien@example.com | I come in peace! | 2025-04-10 18:30:13.382650 |
