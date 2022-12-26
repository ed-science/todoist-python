# -*- coding: utf-8 -*-
from .generic import Manager


class ActivityManager(Manager):
    def get(self, **kwargs):
        """
        Get events from the activity log.
        """
        params = {"token": self.token} | kwargs
        return self.api._get("activity/get", params=params)
