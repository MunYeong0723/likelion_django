=====
Accounts
=====

Accounts is a simple Django app to conduct Web-based Accounts. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "Accounts" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'Accounts',
    ]

2. Include the Accounts URLconf in your project urls.py like this::

    path('Accounts/', include('Accounts.urls')),

3. Run `python manage.py migrate` to create the Accounts models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a account (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/Accounts/ to participate in the account.