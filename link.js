<script>
    function copyLink( id ) {
      /* Get the text field */
      var copyText = document.getElementById( "thislinkhere-" + id );

      /* Select the text field */
      copyText.select();

      /* Copy the text inside the text field */
      document.execCommand( "copy" );

      /* Alert the copied text */
      alert( "Are you sure you want to share this link?: " + copyText.value );
    }
  </script> 