from models.waitlistdb import WaitListDB


class WaitList(object):
    ''' WaitList object '''
    @staticmethod
    def join_to(pid, tid, uid, note):
        ''' Join to

        :param str pid: project id
        :param str tid: team id
        :param str uid: uid
        :param str note: note

        '''
        return WaitListDB().join_to(pid=pid, tid=tid, uid=uid, note=note)

    @staticmethod
    def is_in_wait(pid, tid, uid):
        ''' is in wait list

        :param str pid: project id
        :param str tid: team id
        :param str uid: uid

        '''
        return WaitListDB().is_in_wait(pid=pid, tid=tid, uid=uid)

    def list_by_team(pid, tid, uid=None):
        ''' List team waitting user

        :param str pid: project id
        :param str tid: team id
        :param str uid: uid

        '''
        return WaitListDB().list_by(pid=pid, tid=tid, uid=uid)

    def make_result(wid, pid, uid, result):
        ''' make result

        :param str wid: waitlist id
        :param str pid: project id
        :param str uid: user id
        :param str result: result in approval, deny.

        '''
        return WaitListDB().make_result(_id=wid, pid=pid, uid=uid, result=result)
