"""Error Handling (lib/error.c).

https://github.com/thom311/libnl/blob/libnl3_2_25/lib/error.c

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation version 2.1
of the License.
"""

import errno

import libnl3.errno_

errmsg = dict((i, '') for i in range(libnl3.errno_.NLE_MAX + 1))
errmsg.update({  # https://github.com/thom311/libnl/blob/libnl3_2_25/lib/error.c#L15
    libnl3.errno_.NLE_SUCCESS: 'Success',
    libnl3.errno_.NLE_FAILURE: 'Unspecific failure',
    libnl3.errno_.NLE_INTR: 'Interrupted system call',
    libnl3.errno_.NLE_BAD_SOCK: 'Bad socket',
    libnl3.errno_.NLE_AGAIN: 'Try again',
    libnl3.errno_.NLE_NOMEM: 'Out of memory',
    libnl3.errno_.NLE_EXIST: 'Object exists',
    libnl3.errno_.NLE_INVAL: 'Invalid input data or parameter',
    libnl3.errno_.NLE_RANGE: 'Input data out of range',
    libnl3.errno_.NLE_MSGSIZE: 'Message size not sufficient',
    libnl3.errno_.NLE_OPNOTSUPP: 'Operation not supported',
    libnl3.errno_.NLE_AF_NOSUPPORT: 'Address family not supported',
    libnl3.errno_.NLE_OBJ_NOTFOUND: 'Object not found',
    libnl3.errno_.NLE_NOATTR: 'Attribute not available',
    libnl3.errno_.NLE_MISSING_ATTR: 'Missing attribute',
    libnl3.errno_.NLE_AF_MISMATCH: 'Address family mismatch',
    libnl3.errno_.NLE_SEQ_MISMATCH: 'Message sequence number mismatch',
    libnl3.errno_.NLE_MSG_OVERFLOW: 'Kernel reported message overflow',
    libnl3.errno_.NLE_MSG_TRUNC: 'Kernel reported truncated message',
    libnl3.errno_.NLE_NOADDR: 'Invalid address for specified address family',
    libnl3.errno_.NLE_SRCRT_NOSUPPORT: 'Source based routing not supported',
    libnl3.errno_.NLE_MSG_TOOSHORT: 'Netlink message is too short',
    libnl3.errno_.NLE_MSGTYPE_NOSUPPORT: 'Netlink message type is not supported',
    libnl3.errno_.NLE_OBJ_MISMATCH: 'Object type does not match cache',
    libnl3.errno_.NLE_NOCACHE: 'Unknown or invalid cache type',
    libnl3.errno_.NLE_BUSY: 'Object busy',
    libnl3.errno_.NLE_PROTO_MISMATCH: 'Protocol mismatch',
    libnl3.errno_.NLE_NOACCESS: 'No Access',
    libnl3.errno_.NLE_PERM: 'Operation not permitted',
    libnl3.errno_.NLE_PKTLOC_FILE: 'Unable to open packet location file',
    libnl3.errno_.NLE_PARSE_ERR: 'Unable to parse object',
    libnl3.errno_.NLE_NODEV: 'No such device',
    libnl3.errno_.NLE_IMMUTABLE: 'Immutable attribute',
    libnl3.errno_.NLE_DUMP_INTR: 'Dump inconsistency detected, interrupted',
})


def nl_syserr2nlerr(error_):
    """https://github.com/thom311/libnl/blob/libnl3_2_25/lib/error.c#L84."""
    error_ = abs(error_)
    legend = {
        errno.EBADF: libnl3.errno_.NLE_BAD_SOCK,
        errno.EADDRINUSE: libnl3.errno_.NLE_EXIST,
        errno.EEXIST: libnl3.errno_.NLE_EXIST,
        errno.EADDRNOTAVAIL: libnl3.errno_.NLE_NOADDR,
        errno.ESRCH: libnl3.errno_.NLE_OBJ_NOTFOUND,
        errno.ENOENT: libnl3.errno_.NLE_OBJ_NOTFOUND,
        errno.EINTR: libnl3.errno_.NLE_INTR,
        errno.EAGAIN: libnl3.errno_.NLE_AGAIN,
        errno.ENOTSOCK: libnl3.errno_.NLE_BAD_SOCK,
        errno.ENOPROTOOPT: libnl3.errno_.NLE_INVAL,
        errno.EFAULT: libnl3.errno_.NLE_INVAL,
        errno.EACCES: libnl3.errno_.NLE_NOACCESS,
        errno.EINVAL: libnl3.errno_.NLE_INVAL,
        errno.ENOBUFS: libnl3.errno_.NLE_NOMEM,
        errno.ENOMEM: libnl3.errno_.NLE_NOMEM,
        errno.EAFNOSUPPORT: libnl3.errno_.NLE_AF_NOSUPPORT,
        errno.EPROTONOSUPPORT: libnl3.errno_.NLE_PROTO_MISMATCH,
        errno.EOPNOTSUPP: libnl3.errno_.NLE_OPNOTSUPP,
        errno.EPERM: libnl3.errno_.NLE_PERM,
        errno.EBUSY: libnl3.errno_.NLE_BUSY,
        errno.ERANGE: libnl3.errno_.NLE_RANGE,
        errno.ENODEV: libnl3.errno_.NLE_NODEV,
    }
    return int(legend.get(error_, libnl3.errno_.NLE_FAILURE))
