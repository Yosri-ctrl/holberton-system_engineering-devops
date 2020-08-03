#Kill a process
exec{ 'kill_a_processor':
  command  => 'pkill killmenow',
  provider => 'shell',
}