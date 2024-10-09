from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from .models import *
from .filters import SyslogFilter
from .helper.process_syslog import ProcessSyslog as SysLog
# from .helper.dataframe_to_sqlite import DataframeToSqlite as DfToDb


# Create your views here.

def events(request):
    # template = loader.get_template("syslog.html")
    syslog_df = SysLog().process_syslog()
    syslog_columns = syslog_df.columns.to_list()
    syslog_filters = SyslogFilter(
        request.GET, queryset=SyslogModel.objects.all()
    )
    # DfToDb(syslog_df).dataframe_to_sqlite_db()
    queries = request.GET
    if queries.get("datetime__icontains"):
        syslog_df = syslog_df[
            syslog_df["datetime"].str.lower().str.contains(
                str(queries.get("datetime__icontains")).lower())
        ]
    if queries.get("host__icontains"):
        syslog_df = syslog_df[
            syslog_df["host"].str.lower().str.contains(
                str(queries.get("host__icontains")).lower())
        ]
    if queries.get("type__icontains"):
        syslog_df = syslog_df[
            syslog_df["type"].str.lower().str.contains(
                str(queries.get("type__icontains")).lower())
        ]
    context = {
        "syslog_columns": syslog_columns,
        "syslog_values": syslog_df.values,
        "syslog_filters": syslog_filters,
    }
    return render(request, "syslog.html", context)
    # return HttpResponse(template.render(context, request))
