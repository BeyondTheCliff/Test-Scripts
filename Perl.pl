#!/usr/bin/perl

@ages = (25, 30, 40);             
@names = ("John Paul", "Lisa", "Kumar");
$n = 0;


while ($n != 10) {
	if ($ages[$n] == undef) {
		exit 0;
	} else {
		print "$names[$n] = $ages[$n]\n";
		$n = $n + 1;
	}
}
