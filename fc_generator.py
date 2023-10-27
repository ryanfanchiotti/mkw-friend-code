import hashlib


def fc_generator(pid: int, gid: str = 'RMCJ') -> int:
    """
    Port of the C FC code generator

    :param int pid: 9 digit person id
    :param str gid: 4 char game id, defaults to 'RMCJ'
    :return: int representing FC code

    From C version in http://wiki.tockdom.com/wiki/Friend_Code

    u64 pid_to_fc(u32 pid) {
    if (pid == 0)
     // behaviour observed in MKWii, more likely an error condition
     return 0;
    else {
     u8 buffer[8], md5[16];
     // buffer is pid in little endian, followed by RMCJ in little endian
     buffer[0] = pid >> 0;
     buffer[1] = pid >> 8;
     buffer[2] = pid >> 16;
     buffer[3] = pid >> 24;

     buffer[4] = 'J'; // the reversed online relevant game id
     buffer[5] = 'C';
     buffer[6] = 'M';
     buffer[7] = 'R';

     // md5digest computes the digest of the second parameter and stores it in the first.
     md5digest(md5, buffer, 8);
     return ((u64)(md5[0] >> 1) << 32) | pid;
    }
   }
    """
    assert isinstance(pid, int)
    assert isinstance(gid, str) and len(gid) == 4
    b_pid = pid.to_bytes(length=4, byteorder='little', signed=False)
    b_gid = gid[::-1].encode('utf-8')
    buffer = b_pid + b_gid
    md5 = hashlib.md5(buffer).digest()
    hc = (md5[0] >> 1) << 32
    fc = hc | pid
    return fc
