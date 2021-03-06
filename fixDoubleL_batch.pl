#!/usr/bin/perl

use strict;
use warnings;
use 5.18.0;

# Usage:  
    # 1st Argument: The file to containing the LL words

print STDOUT "================================================================================\n";
print STDOUT "fixDoubleL Script Run at " . localtime() . "\n";

# a function to remove duplicates from an array
sub uniq (@) {
    # From CPAN List::MoreUtils, version 0.22
    my %h;
    map { $h{$_}++ == 0 ? $_ : () } @_;
}

# Get the list of txt or html files in the html directory
my @textfiles;
opendir my $dh, "html" or die "Can't open directory: $!";

while ( readdir $dh ) {
    chomp;
    next if $_ eq '.' or $_ eq '..' or $_ =~ m/_clean\./ or $_ !~ m/\.(html|txt)$/;    
    my $textfile = $_;
    push(@textfiles, $textfile);
    next;
}
my $numfiles = scalar @textfiles;

print STDOUT "* There are $numfiles file(s) to process: ";
print STDOUT join "; ", @textfiles;
print STDOUT ".\n";

# open the text file with the double L words.
my $wordfile = $ARGV[0] ||= "doubleL_words.txt";
open (WFH, '<', $wordfile) or die "Can't open input file '$wordfile': $!";

# import the words into an array
chomp(my @lines = <WFH>);

# close the file again
close WFH or die "Can't close file: $!";

# # create the hash to store the words to correct
my %replace;

for ( @lines ) {
    my $lookup = $_ =~ s/ll/l /gr;
    $replace{$lookup} = $_;
}

# add duplicate entry with first letter capitalised for all existing entries
@replace{ map { ucfirst } keys %replace } = map { ucfirst } values %replace;

# find edge case: words ending in ll that don't have two spaces before next word.
my @ends_with_ll = grep { m/l\s$/ } keys %replace;

# output the number of entries imported
my $num_words = scalar keys %replace;
print STDOUT "* There are $num_words entrie(s) in the \%replace hash from [$wordfile].\n";
print STDOUT "================================================================================\n\n";

my $regex = join "|", map { quotemeta } sort { $b cmp $a } keys %replace;
my $regex_ends_with_ll = join "|", map { quotemeta } sort { $b cmp $a } @ends_with_ll;

$regex = qr/$regex/;
$regex_ends_with_ll = qr/$regex_ends_with_ll/;

# # Open Each Text File
foreach (@textfiles) {
    my $textfile = "html/" . $_;
    my $textfile_out = $textfile =~ s/(\.txt|\.html)/_clean$1/gr;

    print STDOUT "\n\nCleaning [$textfile] and sending output to [$textfile_out]\n";
    print STDOUT "--------------------------------------------------------------------------------\n";

    my $i = 0;
    my @all_matches;
    open (FH, '<', $textfile) or die "Can't open input file '$textfile': $!";
    open (FHOUT, '>', $textfile_out) or die "Can't open output file '$textfile_out': $!";
    while (<FH>) {
        my $line = $_;
        
        my $before = " ???????????????\"-"; # boundary conditions before search term
        my $after = " ,.?????????'???;:?!-"; # boundary conditions after search term

        # get a list of the matches
        my @matches = $line =~ /(?<=[$before])($regex)(?=[$after])/g;
        my @matches_startline = $line =~ /^($regex)(?=[$after])/g;
        my @matches_ends_with_ll = $line =~ /(?<=[$before])($regex_ends_with_ll)(?=\w)/g;
        my @matches_ends_with_ll_startline = $line =~ /^($regex_ends_with_ll)(?=\w)/g;

        # and count them
        my $count = scalar @matches + scalar @matches_startline + 
            scalar @matches_ends_with_ll + scalar @matches_ends_with_ll_startline;

        # fix any words that matched
        $line =~ s/(?<=[$before])($regex)(?=[$after])/$replace{$1}/g;
        $line =~ s/^($regex)(?=[$after])/$replace{$1}/g;
        $line =~ s/(?<=[$before])($regex_ends_with_ll)(?=\w)/$replace{$1} /g; # edge case ends with ll
        $line =~ s/^($regex_ends_with_ll)(?=\w)/$replace{$1} /g; # ends with ll at start of line

        #output the line to the cleaned file
        print FHOUT $line; 

        # count the instance of a match
        $i += $count;
        #add the matches to the list of all matches for the file
        @all_matches = uniq(@all_matches, @matches, @matches_startline, 
                            @matches_ends_with_ll, @matches_ends_with_ll_startline);

    }
    
    close FH or die "Can't close file: $!";
    close FHOUT or die "Can't close file: $_";

    my $uniq = scalar @all_matches; # count unique matches

    print STDOUT "Cleaned $i instances of $uniq words. \n";
    print STDOUT join "; ", @all_matches;
    print STDOUT ".\n\n";
}

print STDOUT "Completed at " . localtime() . "\n";
print STDOUT "================================================================================";
