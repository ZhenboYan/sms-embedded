#! /bin/bash

echo "Starting Crontab setup"
> cron_autopush
echo "#Puppet Name: check internet connection and run python script every 15 seconds" >> cron_autopush
echo "MAILTO=""" >> cron_autopush
echo "* * * * * for i in 0 1 2; do ${PWD}/auto_run.sh & sleep 15; done; ${PWD}/auto_run.sh" >> cron_autopush
crontab cron_autopush
echo "!!    crontab set up successfully"
crond