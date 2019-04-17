capilogs
========

``capilogs`` is a fork of the `apilogs <https://github.com/jorgebastida/awslogs>`_ project which is a fork of the `awslogs <https://github.com/jorgebastida/awslogs>`_ project with specific customizations suited to querying and streaming logs for
Correlated Serverless API calls using `Amazon API Gateway <https://aws.amazon.com/api-gateway/>`_ and `AWS Lambda <https://aws.amazon.com/lambda/>`_.

Simply provide a list of API Gateway API ID and Stage name and `capilogs` will automatically aggregate log events from all log groups & streams for your API Gateway APIS as well as all Lambda function log streams attached to each API.

Installation/Running
--------------------
$ pip install capilogs

i.e. stream logs for your Serverless API:
    $ capilogs get --api-id abc123,xyz123 --stage dev --aws-region us-east-1 --watch

Grep for errors one hour ago using credentials from AWS CLI profile "myprofile":
    $ capilogs get --api-id abc123,xyz123 --stage test2 --profile myprofile --aws-region us-east-1 --start='2h ago' --end='1h ago' --filter-term ERROR


.. image:: https://github.com/rpgreen/apilogs/blob/master/media/apilogs-screenshot.png

Features
--------

* Aggregate logs from across groups & streams.

  - Aggregate all streams in a list of groups.
  - Aggregate streams matching a regular expression.

* Colored output.
* List existing groups

  - ``$ capilogs groups``

* List existing streams

  - ``$ capilogs streams /var/log/syslog``

* Watch logs as they are created

  - ``$ capilogs get /var/log/syslog ALL --watch``

* Human-friendly time filtering:

  - ``--start='23/1/2015 14:23'``
  - ``--start='2h ago'``
  - ``--start='2d ago'``
  - ``--start='2w ago'``
  - ``--start='2d ago' --end='1h ago'``

* Retrieve event metadata:

  - ``--timestamp`` Prints the creation timestamp of each event.
  - ``--ingestion-time`` Prints the ingestion time of each event.

Options
-------

* ``capilogs groups``: List existing groups
* ``capilogs streams GROUP``: List existing streams withing ``GROUP``
* ``capilogs get GROUP [STREAM_EXPRESSION]``: Get logs matching ``STREAM_EXPRESSION`` in ``GROUP``.

  - Expressions can be regular expressions or the wildcard ``ALL`` if you want any and don't want to type ``.*``.

**Note:** You need to provide to all these options a valid AWS region using ``--aws-region`` or ``AWS_REGION`` env variable.


Time options
-------------

While querying for logs you can filter events by ``--start`` ``-s`` and ``--end`` ``-e`` date.

* By minute:

  - ``--start='2m'`` Events generated two minutes ago.
  - ``--start='1 minute'`` Events generated one minute ago.
  - ``--start='5 minutes'`` Events generated five minutes ago.

* By hours:

  - ``--start='2h'`` Events generated two hours ago.
  - ``--start='1 hour'`` Events generated one hour ago.
  - ``--start='5 hours'`` Events generated five hours ago.

* By days:

  - ``--start='2d'`` Events generated two days ago.
  - ``--start='1 day'`` Events generated one day ago.
  - ``--start='5 days'`` Events generated five days ago.

* By weeks:

  - ``--start='2w'`` Events generated two week ago.
  - ``--start='1 week'`` Events generated one weeks ago.
  - ``--start='5 weeks'`` Events generated five week ago.

* Using specific dates:

  - ``--start='23/1/2015 12:00'`` Events generated after midday  on the 23th of January 2015.
  - ``--start='1/1/2015'`` Events generated after midnight on the 1st of January 2015.
  - ``--start='Sat Oct 11 17:13:46 UTC 2003'`` You can use detailed dates too.

  Note, for time parsing awslogs uses `dateutil <https://dateutil.readthedocs.org/en/latest/>`_.

* All previous examples are applicable for  ``--end`` ``-e`` too.

Filter options
----------------

You can use ``--filter-pattern`` if you want to only retrieve logs which match one CloudWatch Logs Filter pattern.
This is helpful if you know precisely what you are looking for, and don't want to download the entire set of streams.

For example, if you only want to download the report events from a Lambda stream you can run::

  $ capilogs get my_lambda_group --filter-pattern="[r=REPORT,...]"


Full documentation of how to write patterns: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html

You can use ``--filter-term`` if you want to only retrieve logs which match one CloudWatch Logs term.
This is helpful if you know precisely what you are looking for, and don't want to download the entire set of streams.
This option takes one of the following values: PERFORM ERROR COST or the correlation-id

For example, if you only want to download the report events from a Lambda stream you can run::

  $ capilogs get my_lambda_group --filter-term ERROR
  $ capilogs get my_lambda_group --filter-term 1234-5678-1234-5678


Contribute
-----------

* Fork the repository on GitHub.
* Write a test which shows that the bug was fixed or that the feature works as expected.

  - Use ``tox`` command to run all the tests in all locally available python version.

* Send a pull request and bug the maintainer until it gets merged and published. :).

For more instructions see `TESTING.rst`.


Helpful Links
-------------

* http://aws.amazon.com/cloudwatch/
* http://boto.readthedocs.org/en/latest/ref/logs.html
* http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_limits.html

How to provide AWS credentials to capilogs
------------------------------------------

Although, the most straightforward thing to do might be use ``--aws-access-key-id`` and ``--aws-secret-access-key`` or ``--profile``, this will eventually become a pain in the ass.

* If you only have one ``AWS`` account, my personal recommendation would be to configure `aws-cli <http://aws.amazon.com/cli/>`_. ``capilogs`` will use those credentials if available.
* If you have multiple ``AWS`` accounts or you don't want to setup ``aws-cli``, I would recommend you to use `envdir <https://pypi.python.org/pypi/envdir>`_ in order to make ``AWS_ACCESS_KEY_ID`` and ``AWS_SECRET_ACCESS_KEY`` available to ``capilogs``.
