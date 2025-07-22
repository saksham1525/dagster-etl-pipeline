import dagster as dg
from dagster_essentials.defs.jobs import trip_update_job
from dagster_essentials.defs.jobs import weekly_update_job

trip_update_schedule = dg.ScheduleDefinition(
    job=trip_update_job,
    cron_schedule="0 0 5 * *"
)
weekly_update_schedule = dg.ScheduleDefinition(
    job=weekly_update_job,
    cron_schedule="0 0 * * 1"
)