PowerLinux / OpenPOWER Request Form
===================================
:slug: services/powerdev/request_gpu
:title: OpenPOWER GPU Request Form
:menu: POWERLinux/OpenPOWER Development Hosting, OpenPOWER GPU Request Form, 3

.. raw:: html

    <div id="content">
    <!-- Formsender error script -->
    <script src="../../../theme/js/formsender-error.js"></script>
      <div class="field field-name-body field-type-text-with-summary field-label-hidden">
        <div class="field-items">
          <div class="field-item even" property="content:encoded">
          <p>Description here.</p>
          </div>
        </div>
      </div>
      <form class="webform-client-form" enctype="multipart/form-data" action="http://formsender.osuosl.org:80" method="post" id="webform-client-form-1086" accept-charset="UTF-8">
        <div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-name">
            <label for="edit-submitted-name">Name <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-name" name="name" value="" size="60" maxlength="128" class="form-text required" />
          </div>
          <div class="form-item webform-component webform-component-email" id="webform-component-email">
            <label for="edit-submitted-email">Email <span class="form-required" title="This field is required.">*</span></label>
            <input class="email form-text form-email required" type="email" id="edit-submitted-email" name="email" size="60" />
          </div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-project-name">
            <label for="edit-submitted-project-name">Project Name <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-project-name" name="project_name" value="" size="60" maxlength="128" class="form-text required" />
            <div class="description">Name of the open source project or education institution this request will be supporting.</div>
          </div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-project-url">
            <label for="edit-submitted-project-url">Project URL <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-project-url" name="project_url" value="" size="60" maxlength="128" class="form-text required" />
            <div class="description">Primary website URL for the open source project or education institution.</div>
          </div>
          <div class="form-item webform-component webform-component-textarea" id="webform-component-usage">
            <label for="edit-submitted-usage">Expected Usage Model <span class="form-required" title="This field is required.">*</span></label>
            <div class="form-textarea-wrapper resizable"><textarea id="edit-submitted-usage" name="expected_usage_model" cols="60" rows="5" class="form-textarea required"></textarea></div>
            <div class="description">What types of activity will the machine be used for? (i.e. compile builds, performance testing, architecture troubleshooting, etc).</div>
          </div>
          <div class="form-item webform-component webform-component-textfield" id="webform-component-duration">
            <label for="edit-submitted-duration">Anticipated duration of need <span class="form-required" title="This field is required.">*</span></label>
            <input type="text" id="edit-submitted-duration" name="anticipated_duration_of_need" value="" size="60" maxlength="128" class="form-text required" />
            <div class="description">How long do you expect you will need these resources? Ongoing or indefinitely are also acceptable answers.</div>
          </div>
          <div class="form-item webform-component webform-component-number" id="webform-component-num-nodes">
            <label for="edit-submitted-num-nodes">Number of nodes <span class="form-required" title="This field is required.">*</span></label>
            <input type="number" id="edit-submitted-num-nodes" name="number_of_nodes" value="1" min="1" step="any" class="form-text form-number required" />
            <div class="description">Estimated number of nodes (machines) you'd like to have.</div>
          </div>
          <div class="form-item webform-component webform-component-select" id="webform-component-distribution">
            <label for="edit-submitted-distribution">Distribution <span class="form-required" title="This field is required.">*</span></label>
            <select id="edit-submitted-distribution" name="distribution" class="form-select required">
              <option value="None selected" selected="selected">- Select -</option>
              <option value="Fedora">Fedora</option>
              <option value="CentOS">CentOS</option>
              <option value="Debian">Debian</option>
              <option value="Ubuntu">Ubuntu</option>
              <option value="OpenSUSE">OpenSUSE</option>
              <option value="Other">Other</option>
            </select>
            <div class="description">Which Linux distribution would you like to use for your machine? This would likely be the latest stable version available for PPC. If you want a specific version, please state that in the comments section on the last page.</div>
          </div>
          <div class="form-item webform-component webform-component-textarea" id="webform-component-ssh-key">
            <label for="edit-submitted-ssh-key">SSH Public Key <span class="form-required" title="This field is required.">*</span></label>
            <div class="form-textarea-wrapper resizable"><textarea id="edit-submitted-ssh-key" name="ssh_public_key" cols="60" rows="5" class="form-textarea required"></textarea></div>
            <div class="description">Public SSH key to be used for initial access to the system.</div>
          </div>
          <div class="form-item webform-component webform-component-select" id="webform-component-deployment-timeframe">
            <label for="edit-submitted-deployment-timeframe">Deployment timeframe </label>
            <select id="edit-submitted-deployment-timeframe" name="deployment_timeframe" class="form-select">
              <option value="Within 7 business Days" selected="selected">Within 7 business Days</option>
              <option value="Within 3 business Days">Within 3 business Days</option>
              <option value="Within 1 business Days">Within 1 business Day</option>
            </select>
            <div class="description">Normal turnaround for access is typically 7 business days. If you need it sooner than that, please choose which time frame you need. We will do our best to accommodate your request. </div>
          </div>
          <div class="form-item webform-component webform-component-textarea" id="webform-component-other-information">
            <label for="edit-submitted-other-information">Other information </label>
            <div class="form-textarea-wrapper resizable"><textarea id="edit-submitted-other-information" name="other_information" cols="60" rows="5" class="form-textarea"></textarea></div>
            <div class="description">Is there anything additional you would like to provide for your request?</div>
          </div>

          <p><i>You should receive an automated email from our request ticketing system to the email address you have provided
          within 5-10 minutes.  If you don't receive this email please reach out to us at <a href="mailto:openpower-gpu-support@osuosl.org">openpower-gpu-support@osuosl.org</a> or
          via IRC in <b>#osuosl</b> on Freenode.</i></p>

          <!-- Formsender Settings -->
          <input type="hidden" name="last_name" value="" />
          <input type="hidden" name="token" value="15674hsda//*q23%^13jnxccv3ds54sa4g4sa532323!OoRdsfISDIdks38*(dsfjk)aS" />
          <!-- The following must be set to http://www.osuosl.org/services/powerdev/request_gpu in production -->
          <input type="hidden" name="redirect" value="http://www.osuosl.org/services/powerdev/request_gpu" />
          <input type="hidden" name="mail_subject_prefix" value="New OpenPOWER GPU Request" />
          <input type="hidden" name="mail_subject_key" value="project_name" />
          <input type="hidden" name="send_to" value="openpower_gpu" />
          <!-- /Formsender Settings -->

          <div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit" name="op" value="Submit" class="form-submit" /></div>
        </div>
      </form>
    </div>
