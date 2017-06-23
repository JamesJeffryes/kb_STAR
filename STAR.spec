/*
   Name of module: STAR

   This KBase module wraps the free open source software STAR: ultrafast universal RNA-seq aligner.
   STAR-2.5.3a

   References:
   https://github.com/alexdobin/STAR/
   https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf
*/

module STAR {
    /* 
        A 'typedef' allows you to provide a more specific name for
        a type.  Built-in primitive types include 'string', 'int',
        'float'.  Here we define a type named assembly_ref to indicate
        a string that should be set to a KBase ID reference to an
        Assembly data object.
    */
    typedef string assembly_ref;

    /* A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
		    
    typedef int boolean;

	        /* An X/Y/Z style reference
    */
    typedef string obj_ref;

    /*
	Will align the input reads (or set of reads specified in a SampleSet) to the specified
        assembly or assembly for the specified Genome (accepts Assembly, ContigSet, or Genome types)
        and produces a ReadsAlignment object, or in the case of a SampleSet, a ReadsAlignmentSet
        object

	obj_ref genome_ref: KBase workspace reference genome to align reads against
	obj_ref sampleset_ref: the workspace reference for the sampleset of reads to align, referring to 
		either a SingleEnd/PairedEnd reads, or a SampleSet, or a ReadsSet input
	string workspace_name: the workspace name provided by the narrative for housing output in KBase
	string output_name - name of the output ReadsAlignment or ReadsAlignmentSet
	
	string outFileNamePrefix: you can change the file prefixes using --outFileNamePrefix /path/to/output/dir/prefix
                By default, this parameter is ./, i.e. all output files are written in current directory without a prefix
	string quantMode: types of quantification requested--none/TranscriptomeSAM/GeneCounts
	int outFilterMultimapNmax: max number of multiple alignments allowed for a read: if exceeded, 
		the read is considered unmapped, default to 20
	int alignSJoverhangMin: minimum overhang for unannotated junctions, default to 8
	int alignSJDBoverhangMin: minimum overhang for annotated junctions, default to 1
	int outFilterMismatchNmax: maximum number of mismatches per pair, large number switches off this filter, default to 999
	int alignIntronMin: minimum intron length, default to 20
	int alignIntronMax: maximum intron length, default to 1000000
	int alignMatesGapMax: maximum genomic distance between mates, default to 1000000
		
	@optional quantMode
	@optional alignSJoverhangMin
	@optional alignSJDBoverhangMin
	@optional outFilterMismatchNmax	
	@optional alignIntronMin
	@optional alignIntronMax
	@optional alignMatesGapMax
	@optional outFileNamePrefix
    */
    typedef structure {
        obj_ref sampleset_ref;
        obj_ref genome_ref;
        string workspace_name;
	string output_name;
    
	string quantMode;
	int outFilterMultimapNmax;
	int alignSJoverhangMin;
	int alignSJDBoverhangMin;
	int outFilterMismatchNmax;
	int alignIntronMin;
	int alignIntronMax;
	int alignMatesGapMax;
	string outFileNamePrefix;
    } STARParams;

    /*
        Here is the definition of the output of the function.  The output
        can be used by other SDK modules which call your code, or the output
        visualizations in the Narrative.  'report_name' and 'report_ref' are
        special output fields- if defined, the Narrative can automatically
        render your Report.
			
	output_folder: folder path that holds all files generated by STAT	
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
    */
    typedef structure {
	string output_folder;
	obj_ref alignment_ref;
        string report_name;
        string report_ref;
    } STARResults;
    
    /*
        The actual function is declared using 'funcdef' to specify the name
        and input/return arguments to the function.  For all typical KBase
        Apps that run in the Narrative, your function should have the 
        'authentication required' modifier.
    */
    funcdef run_star(STARParams params)
        returns (STARResults output) authentication required;

};
