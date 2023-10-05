def main():
  print('READ ALL THE PRINTS CAREFULLY')
  realname = input('Please enter the main part of username eg can be like jacob in jacob200: ')
  Anothermain = input('Does it have another main part? eg ninja in ninjamike8764 y/n:')
  if Anothermain == 'y':
    Anothermain2 = input('Say the other main part:')
  cooladjective = input('Does it have any adjective like eg cool in coolninja123? y/n:')
  if cooladjective == 'y':
   ADJECTIVE90 = input('say the adjective:')
  answer1 = input('do you want four digit method? y/n:')
  if answer1 == 'y':
    FOURDIGITCODE1 = input('Please enter the two of the four digit method: ')
  if answer1 == 'y':
   FOURDIGITCODE2 = input('Please enter the other two of the four digit method: ')
  if answer1 == 'y' and cooladjective == 'y' and Anothermain == 'n':
    print('Your possible password:')
    print('123' + realname, realname + '123', realname + FOURDIGITCODE1, realname + FOURDIGITCODE2, realname + 'is' + ADJECTIVE90, '123' + realname + FOURDIGITCODE1, '123' + realname + FOURDIGITCODE2, realname + FOURDIGITCODE1 + '123', realname + FOURDIGITCODE2 + '123', realname + 'is' + ADJECTIVE90 + FOURDIGITCODE1, realname + 'is' + ADJECTIVE90 + FOURDIGITCODE2, FOURDIGITCODE1 + realname + 'is' + ADJECTIVE90, FOURDIGITCODE2 + realname + 'is' + ADJECTIVE90, realname + 'is' + ADJECTIVE90 + '123', '123' + realname + 'is' + ADJECTIVE90, 'im' + ADJECTIVE90, '123' + 'im' + ADJECTIVE90, 'im' + ADJECTIVE90 + '123', FOURDIGITCODE1 + 'im' + ADJECTIVE90, FOURDIGITCODE2 + 'im' + ADJECTIVE90, 'im' + ADJECTIVE90 + FOURDIGITCODE1, 'im' + ADJECTIVE90 + FOURDIGITCODE2, FOURDIGITCODE1 + 'im' + ADJECTIVE90 + '123', FOURDIGITCODE2 + 'im' + ADJECTIVE90 + '123', '123' + 'im' + ADJECTIVE90 + FOURDIGITCODE1, '123' + 'im' + ADJECTIVE90 + FOURDIGITCODE2)
  if answer1 == 'n' and cooladjective == 'n' and Anothermain == 'n':
   print('Your possible passwords:')
   print('possible passwords:', realname + '123', '123' + realname)
  if answer1 == 'n' and cooladjective == 'y' and Anothermain == 'n':
   print('your possible passwords')
   print('123' + realname + 'is' + ADJECTIVE90, realname + 'is' + ADJECTIVE90, realname + '123', '123' + realname, realname + 'is' + ADJECTIVE90 + '123', 'im' + ADJECTIVE90 + '123', '123' + 'im' + ADJECTIVE90, 'im' + ADJECTIVE90)
  if cooladjective == 'n' and answer1 == 'y' and Anothermain == 'n':
    print('your possible passwords')
    print('123' + realname + FOURDIGITCODE1, '123' + realname + FOURDIGITCODE2, realname + '123' + FOURDIGITCODE1, realname + '123' + FOURDIGITCODE2, realname + FOURDIGITCODE1, realname + FOURDIGITCODE2 +  '.')
  if cooladjective == 'y' and answer1 == 'y' and Anothermain == 'y':
    print('Your possible passwords:', Anothermain2 + '123', '123' + Anothermain2, realname + '123', '123' + realname, '123' + Anothermain2 + FOURDIGITCODE1, '123' + realname + FOURDIGITCODE1, '123' + realname + FOURDIGITCODE2, '123' + Anothermain2 + FOURDIGITCODE2, FOURDIGITCODE1 + realname + '123', FOURDIGITCODE1 + Anothermain2 + '123', FOURDIGITCODE2 + realname + '123', FOURDIGITCODE2 + Anothermain2 + '123', realname + FOURDIGITCODE1, Anothermain2 + FOURDIGITCODE1, realname + FOURDIGITCODE2, Anothermain2 + FOURDIGITCODE2, FOURDIGITCODE1 + realname, FOURDIGITCODE1 + Anothermain2, FOURDIGITCODE2 + realname, FOURDIGITCODE2 + Anothermain2, realname + 'is' + ADJECTIVE90, Anothermain2 + 'is' + ADJECTIVE90, '123' + realname + 'is' + ADJECTIVE90 + FOURDIGITCODE1, '123' + realname + 'is' + ADJECTIVE90 + FOURDIGITCODE2, '123' + Anothermain2 + 'is' + ADJECTIVE90 + FOURDIGITCODE1, '123' + Anothermain2 + 'is' + ADJECTIVE90 + FOURDIGITCODE2, FOURDIGITCODE1 + realname + 'is' + ADJECTIVE90 + '123', Anothermain2 + 'is' + ADJECTIVE90 + '123', realname + 'is' + ADJECTIVE90 + '123', '123' + realname + 'is' + ADJECTIVE90, 'im' + ADJECTIVE90, '123' + 'im' + ADJECTIVE90, 'im' + ADJECTIVE90 + '123', FOURDIGITCODE1 + 'im' + ADJECTIVE90, FOURDIGITCODE2 + 'im' + ADJECTIVE90, FOURDIGITCODE1 + 'im' + ADJECTIVE90 + '123', FOURDIGITCODE2 + 'im' + ADJECTIVE90 + '123')
  if cooladjective == 'y' and answer1 == 'n' and Anothermain == 'y':
    print('Your possible passwords:', Anothermain2 + '123', '123' + Anothermain2, realname + '123', '123' + realname, realname + 'is' + ADJECTIVE90, Anothermain + 'is' + ADJECTIVE90, realname + 'is' + ADJECTIVE90 + '123', '123' + realname + 'is' + ADJECTIVE90, Anothermain2 + 'is' + ADJECTIVE90 + '123', '123' + Anothermain2 + 'is' + ADJECTIVE90)
  if cooladjective == 'n' and answer1 == 'y' and Anothermain == 'y':
    print('Your possible passwords:', '123' + realname, realname + '123', Anothermain2 + '123', '123' + Anothermain2, realname + FOURDIGITCODE1, realname + FOURDIGITCODE2, Anothermain2 + FOURDIGITCODE1, Anothermain2 + FOURDIGITCODE2, '123' + realname + FOURDIGITCODE1, '123' + realname + FOURDIGITCODE2, '123' + Anothermain2 + FOURDIGITCODE1, '123' + Anothermain2 + FOURDIGITCODE2, FOURDIGITCODE1 + realname + '123', FOURDIGITCODE2 + realname + '123', FOURDIGITCODE1 + Anothermain2 + '123', FOURDIGITCODE2 + Anothermain2 + '123')
  if cooladjective == 'n' and answer1 == 'n' and Anothermain == 'y':
    print('Your possible passwords:', '123' + realname, realname + '123', Anothermain2 + '123', '123' + Anothermain2)
  print('Usually has updates, if you have any ideias js contact me on discord, my discord: bazingers')
  print('inspired by kyanites /common command and made by bazingers on discord')
  reset = input('Do you want to restart? y/n:')
  print(''

                                          '')
  if reset == 'y':
    main()
  if reset == 'n':
    input('press enter to close :D')
main()
#currently no bugs on the code if any screenshot the things that you did y/n in and send it over to Bazingers on discord
