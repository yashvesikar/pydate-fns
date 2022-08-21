# import datetime
# from typing import Literal
#
#
# class TimeDelta(datetime.timedelta):
#     def __init__(
#         self,
#         **kwargs: dict[
#             Literal["years", "months", "weeks", "days", "hours", "minutes", "seconds"],
#             int,
#         ]
#     ):
#         self.years = kwargs.pop("years", 0)
#         self.months = kwargs.pop("months", 0)
#         self.timedelta = super().__init__(**kwargs)
#
#     def __add__(self, other: datetime.timedelta) -> datetime.timedelta:
#         _result = super().__add__(other)
#         result =
#
